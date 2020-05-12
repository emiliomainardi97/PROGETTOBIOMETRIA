import argparse
import time,pickle
import Concatena,pandas
import cv2
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

    #immagini da classificare
    input_image = cv2.imread('coppia.jpg')  # B,G,R order

    body_parts, all_peaks, subset, candidate = extract_parts(input_image, params, model, model_params)
    canvas, dict, lis1, lis2 = draw(input_image, all_peaks, subset, candidate)

    cv2.imwrite(output, canvas)

    Concatena.salva_csv_dist(lis1, lis2, 'none')

    dataframe = pandas.read_csv("dataset_dist.csv")

    dataset = dataframe.values

    riga = dataframe.shape[0]

    X = dataset[:, 0:93]

    toc = time.time()
    print('processing time is %.5f' % (toc - tic))

    filename = 'finalized_modelRF.sav'
    # load the model from disk
    loaded_model = pickle.load(open(filename, 'rb'))
    predictions = loaded_model.predict(X)
    print(predictions[len(X)-1])