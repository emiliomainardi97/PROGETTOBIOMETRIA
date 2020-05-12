import argparse
import time, pandas,Concatena

import CalcoloCombinazioni, CalcoloDistanza, DeterminaSogliaMedia
from keras.engine.saving import model_from_json

from sklearn import preprocessing

import numpy as np

import cv2, util

from processing import extract_parts, draw

from config_reader import config_reader
from model.cmu_model import get_testing_model

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--image', type=str, help='input image')
    parser.add_argument('--output', type=str, default='result.png', help='output image')
    parser.add_argument('--model', type=str, default='model/model.h5', help='path to the weights file')

    args = parser.parse_args()
    image_path = args.image
    output = args.output
    keras_weights_file = args.model

    tic = time.time()
    print('start processing...')

    # load model

    # authors of original model don't use
    # vgg normalization (subtracting mean) on input images
    model = get_testing_model()
    model.load_weights(keras_weights_file)

    # load config
    params, model_params = config_reader()

    input_image = cv2.imread('quattro1.jpg')  # B,G,R order

    json_file = open('model4.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    loaded_model.load_weights("model4.h5")
    print("Loaded model from disk")

    loaded_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

    body_parts, all_peaks, subset, candidate = extract_parts(input_image, params, model, model_params)
    canvas, dict, lis1, lis2 = draw(input_image, all_peaks, subset, candidate)

    soglia = 0.3

    #recupero combinazioni persone dall'immagine e relative coordinate
    listaCoppie, combinazioni = CalcoloCombinazioni.calcoloFinale(all_peaks)

    for i in range(len(listaCoppie)):
        print(listaCoppie[i])

    print(combinazioni)

    for i in range(len(listaCoppie)):
        print(combinazioni[i])
        dist1,list1 = CalcoloDistanza.selectPlayer1(listaCoppie[i])
        dist2,list2 = CalcoloDistanza.selectPlayer2(listaCoppie[i])

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
            else:
                print("notfight")
        else:
            print("notfight senza classificazione")

    cv2.imwrite(output, canvas)

    cv2.destroyAllWindows()