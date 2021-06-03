import numpy as np 
import matplotlib.pyplot as plt 
import os
import cv2
from sys import argv, stdin, stdout
import random
import pickle 

#DATADIR = "./Tumores-Negativos/"
CATEGORIES = ["Benign","Malignant","Normal"]
OPTIONS = {'-n', '-s'}
OPTION_PROMPT = 'Forneça opção (-n, -s): '

class load_images():
    def __init__(self,path,size,step):
        self._default_path = path
        self._default_step = step
        self._default_size = size
        self._width = 0
        self._height = 0
        self._training_data = []

    def create_training_data(self):
        for category in CATEGORIES:
            path = os.path.join(self._default_path,category) #Caminho dos tipos de cancer
            class_num = CATEGORIES.index(category)
            for img in os.listdir(path):#interator de cada imagem benigna,maligno e normal
                try:
                    img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)#converte para array
                    #Ou utiliza o msm ai de cima sem o cv2.IMREAD_GRAYSCALE ai ele volta ao normal
                    new_array = cv2.resize(img_array, (self._width, self._height)) 
                    #O new array reduz a imagem em 50% ficando pixelada
                    self._training_data.append([new_array, class_num])
                except Exception as e:
                    pass 
        return self._training_data

    def resize_image(self,training_data):
        self_training_data = training_data
        for category in CATEGORIES:
            path = os.path.join(self._default_path, category) #Caminho dos tipos de cancer
            for img in os.listdir(path): #interator de cada imagem benigna,maligno e normal
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                #Ou utiliza o msm ai de cima sem o cv2.IMREAD_GRAYSCALE ai ele volta ao normal
                plt.imshow(img_array, cmap="gray")
                plt.show()
                break
            break   
        #IMG_SIZE = 70 363x244
        print('Tamanho Imagem:',self._default_size)
        self._width = int(1024*int(self._default_size)/100)
        self._height = int(1024*int(self._default_size)/100)
        new_array = cv2.resize(img_array, (self._width, self._height))
        return new_array


    

