import numpy as np 
import matplotlib.pyplot as plt 
import os
import cv2
from sys import argv, stdin, stdout
import random
import pickle 

#DATADIR = "./Tumores-Negativos/"
CATEGORIES = ["Anomalia","Normal"]
OPTIONS = {'-n', '-s'}
OPTION_PROMPT = 'Forneça opção (-n, -s): '

class load_images():
    def __init__(self,path,step):
        self.default_path = path
        self.default_step = step
        self.width = 0
        self.height = 0
        self.training_data = []

    def create_training_data(self):
        for category in CATEGORIES:
            path = os.path.join(self.default_path,category) #Caminho dos tipos de cancer
            class_num = CATEGORIES.index(category)
            for img in os.listdir(path):#interator de cada imagem benigna,maligno e normal
                try:
                    teste = cv2.imread(os.path.join(path, img), cv2.IMREAD_UNCHANGED)
                    self.width = int(teste.shape[0])
                    self.height = int(teste.shape[1])
                    img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)#converte para array
                    dim = img_array.shape #Ou utiliza o msm ai de cima sem o cv2.IMREAD_GRAYSCALE ai ele volta ao normal
                    new_array = img_array #O new array reduz a imagem em 50% ficando pixelada
                    self.training_data.append([new_array, class_num])
                except Exception as e:
                    pass 
        return self.training_data

    def resize_image(self,training_data):
        self.training_data = training_data
        for category in CATEGORIES:
            path = os.path.join(self.default_path, category) #Caminho dos tipos de cancer
            for img in os.listdir(path): #interator de cada imagem benigna,maligno e normal
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)#Ou utiliza o msm ai de cima sem o cv2.IMREAD_GRAYSCALE ai ele volta ao normal
                self.height=img_array.shape[0]
                self.width=img_array.shape[1]
                plt.imshow(img_array, cmap="gray")
                plt.show()
                break
            break   
        return img_array


    

