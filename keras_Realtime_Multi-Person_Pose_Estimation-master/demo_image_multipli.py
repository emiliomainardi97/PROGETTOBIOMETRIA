import argparse
import time

import CalcoloCombinazioni, CalcoloDistanza, DeterminaSogliaMedia

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

    body_parts, all_peaks, subset, candidate = extract_parts(input_image, params, model, model_params)
    canvas, dict, lis1, lis2 = draw(input_image, all_peaks, subset, candidate)

    #recupero combinazioni persone dall'immagine e relative coordinate
    listaCoppie, combinazioni = CalcoloCombinazioni.calcoloFinale(all_peaks)

    for i in range(len(listaCoppie)):
        print(listaCoppie[i])

    print(combinazioni)

    for i in range(len(listaCoppie)):
        print(combinazioni[i])
        dist1,list1 = CalcoloDistanza.selectPlayer1(listaCoppie[i])
        dist2,list2 = CalcoloDistanza.selectPlayer2(listaCoppie[i])
        print(dist1)
        print(dist2)
        temp = np.concatenate((dist1, dist2), axis=0)
        print(DeterminaSogliaMedia.control(temp))

    toc = time.time()
    print('processing time is %.5f' % (toc - tic))

    cv2.imwrite(output, canvas)

    cv2.destroyAllWindows()