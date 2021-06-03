import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle
NAME = "Benign-Malign-Normal-CNN"

class Model:
    '''Default Model for Mammograph Classification'''
    def __init__(self):
        pass
    
    def architeture(self,x, default_steps:int, y):
        model = Sequential()
        X = x/255.0
        print(X.shape[1:])
        model.add(Conv2D(16, (3, 3), input_shape=X.shape[1:]))
        model.add(Activation("relu"))
        model.add(Conv2D(24, (3, 3) , padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(32, (3, 3), padding="same"))
        model.add(Activation("relu"))
        model.add(Conv2D(64, (3, 3), padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Conv2D(64, (3, 3), padding="same"))
        model.add(Activation("relu"))
        model.add(Conv2D(128, (3, 3), padding="same"))
        model.add(Activation("relu"))
        model.add(Conv2D(128, (3, 3), padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        '''
        model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors
        model.add(Dense(32, activation = 'relu')) # Adicionar essa relu aumenta em 0.02 a accuracia
        model.add(Dense(3, activation='softmax'))
        model.add(Activation('softmax'))'''

        model.add(Flatten())
        model.add(Dense(256))
        model.add(Activation("relu"))
        #model.add(Dropout(0.5))
        # softmax classifier
        model.add(Dense(3))
        model.add(Activation("softmax"))
        
        tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))
        model.compile(loss='sparse_categorical_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])

        model.fit(X, y, batch_size=32, epochs=default_steps, validation_split=0.3, callbacks=[tensorboard])
        model.save('Mamogram.Model')