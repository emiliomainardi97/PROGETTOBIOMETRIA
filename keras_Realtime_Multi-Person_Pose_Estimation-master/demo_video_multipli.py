import os
import sys
import argparse
import cv2
import time
from config_reader import config_reader
import CalcoloCombinazioni

import numpy as np

from keras.engine.saving import model_from_json

import pandas, DeterminaSogliaMedia, CalcoloDistanza

from sklearn import preprocessing

import Concatena

from processing import extract_parts, draw

from model.cmu_model import get_testing_model

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

currentDT = time.localtime()
start_datetime = time.strftime("-%m-%d-%H-%M-%S", currentDT)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--video', type=str, help='input video file name')
    parser.add_argument('--model', type=str, default='model/model.h5', help='path to the weights file')
    parser.add_argument('--frame_ratio', type=int, default=1, help='analyze every [n] frames')
    parser.add_argument('--process_speed', type=int, default=4,
                        help='Int 1 (fastest, lowest quality) to 4 (slowest, highest quality)')
    parser.add_argument('--end', type=int, default=None, help='Last video frame to analyze')

    args = parser.parse_args()

    keras_weights_file = args.model
    frame_rate_ratio = args.frame_ratio
    process_speed = args.process_speed
    ending_frame = args.end

    print('start processing...')

    # Video input
    video_path = 'videos/lotta.mp4'
    video_file = video_path

    # Output location
    output_path = 'videos/outputs/'
    output_format = '.mp4'
    video_output = output_path + str(start_datetime) + output_format

    # load model
    # authors of original model don't use
    # vgg normalization (subtracting mean) on input images
    model = get_testing_model()
    model.load_weights(keras_weights_file)

    # load config
    params, model_params = config_reader()

    # Video reader
    cam = cv2.VideoCapture(video_file)
    input_fps = cam.get(cv2.CAP_PROP_FPS)
    ret_val, orig_image = cam.read()
    video_length = int(cam.get(cv2.CAP_PROP_FRAME_COUNT))

    if ending_frame is None:
        ending_frame = video_length

    # Video writer
    output_fps = input_fps / frame_rate_ratio
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(video_output, fourcc, output_fps, (orig_image.shape[1], orig_image.shape[0]))

    scale_search = [1, .5, 1.5, 2]  # [.5, 1, 1.5, 2]
    scale_search = scale_search[0:process_speed]

    params['scale_search'] = scale_search

    json_file = open('model4.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    loaded_model.load_weights("model4.h5")
    print("Loaded model from disk")

    loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    fight = 0
    notfight = 0

    soglia = 0.3

    i = 0  # default is 0
    while(cam.isOpened()) and ret_val is True and i < ending_frame:
        if i % frame_rate_ratio == 0:

            input_image = cv2.cvtColor(orig_image, cv2.COLOR_RGB2BGR)

            tic = time.time()

            boolFight = False

            # generate image with body parts
            body_parts, all_peaks, subset, candidate = extract_parts(input_image, params, model, model_params)
            canvas,dict,lis1,lis2 = draw(orig_image, all_peaks, subset, candidate)

            print('Processing frame: ', i)
            toc = time.time()
            print('processing time is %.5f' % (toc - tic))

            # recupero combinazioni persone dall'immagine e relative coordinate
            listaCoppie, combinazioni = CalcoloCombinazioni.calcoloFinale(all_peaks)

            out.write(canvas)

            for j in range(len(listaCoppie)):
                print(combinazioni[j])
                dist1, list1 = CalcoloDistanza.selectPlayer1(listaCoppie[j])
                dist2, list2 = CalcoloDistanza.selectPlayer2(listaCoppie[j])

                temp = np.concatenate((dist1, dist2), axis=0)
                if DeterminaSogliaMedia.control(temp) >= soglia:
                    Concatena.salva_csv_dist(dist1, dist2, 'none')

                    dataframe = pandas.read_csv("dataset_dist.csv")

                    dataset = dataframe.values

                    riga = dataframe.shape[0]

                    X = dataset[:, 0:93]

                    predictions = loaded_model.predict_classes(X)

                    last = predictions[riga - 1]

                    if (last == 0):
                        print("fight")
                        boolFight = True
                    else:
                        print("notfight")
                else:
                    print("notfight senza classificazione")

            if (boolFight):
                fight = fight + 1
                print("Frame fight")
            else:
                notfight = notfight + 1
                print("Frame notfight")

        print("Fine frame")

        ret_val, orig_image = cam.read()

        i += 1

    if fight > notfight:
        print("FIGHT VIDEO")
    else:
        print("NOTFIGHT VIDEO")