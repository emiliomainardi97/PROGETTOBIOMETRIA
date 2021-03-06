import argparse
import time
import cv2,os
import Concatena
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

    list = os.listdir('C:\Frame_Estratti\\Violence')

    start = 0
    end = 0

    for i in range(start,end):
        path = 'C:\Frame_Estratti\\Violence\\' + list[i]

        input_image = cv2.imread(path)  # B,G,R order

        body_parts, all_peaks, subset, candidate = extract_parts(input_image, params, model, model_params)
        canvas, dict, list1, list2 = draw(input_image, all_peaks, subset, candidate)
        # ISTANZIARE IL DATASET-COMPLETO & DISTANZE
        Concatena.salva_csv(dict,'fight')
        Concatena.salva_csv_dist(list1,list2,'fight')
        print(list[i])
        toc = time.time()
        print('processing time is %.5f' % (toc - tic))
        print(i)

