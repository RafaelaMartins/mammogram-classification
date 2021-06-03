import cv2
import tensorflow as tf
from parse import Parser
from sys import argv, stdin, stdout
import matplotlib.pyplot as plt 
import os
import cv2

CATEGORIES = ["Benign","Malignant","Normal"]

def prepare(filepath, size):
    #IMG_SIZE = 50  # 70 in txt-based
    width = int(1024*size/100)
    height = int(1024*size/100)
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (width, height))
    return new_array.reshape(-1, width, height, 1)

def main(argv):
    parser = Parser()
    options = {}
    options = parser.read_args_validation(argv)
    model = tf.keras.models.load_model("Mamogram.Model")
    if options is not None:
        image_path = options['image_path']
        size = options['size']
        prediction = model.predict([prepare(image_path, size)])
        print(prediction)  # will be a list in a list.
        print(CATEGORIES[int(prediction[0][0])])
       

if __name__ == "__main__":
    main(argv[1:])