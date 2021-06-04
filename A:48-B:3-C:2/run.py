from sys import argv, stdin, stdout
import numpy as np 
import matplotlib.pyplot as plt 
import os
import cv2
from sys import argv, stdin, stdout
import random
from parse import Parser
from load_image import load_images
from galacticModelII import GalacticModelII
import pickle

def main(argv):
    default_steps = 50
    default_size = 96
    default_path = './dataset/'
    parser = Parser()
    options = {}
    options = parser.read_args(argv)

    if options is not None:
        if options['path'] is not False:
            default_steps = options['epoch']
            #default_size = options['size']
            default_path = options['path']
        else:
            default_steps = options['epoch']
            #default_size = options['size']
    else:
        print(default_steps)
        #print(default_size)
        print(default_path)

    data = load_images(default_path,default_steps)
    training_data = []
    new_array = data.resize_image(training_data)
    plt.imshow(new_array, cmap="gray")
    plt.show()  
    training_data =  data.create_training_data()
    print('teste:', len(training_data))   
    random.shuffle(training_data)
    x = []
    y = []

    for features, labels in data.training_data:
        x.append(features)
        y.append(labels)
    
    x = np.array(x).reshape(-1, data.width, data.height,1) 

    pickle_out = open("x.pickle","wb")
    pickle.dump(x, pickle_out)
    pickle_out.close()

    pickle_out = open("y.pickle","wb")
    pickle.dump(y, pickle_out)
    pickle_out.close()

    pickle_in  = open("x.pickle","rb")
    x = pickle.load(pickle_in)

    pickle_in = open("y.pickle","rb")
    y = pickle.load(pickle_in)
    print("chamou Galactic")
    model = GalacticModelII()
    model.architeture(x, default_steps, y)



if __name__ == "__main__":
    main(argv[1:])
