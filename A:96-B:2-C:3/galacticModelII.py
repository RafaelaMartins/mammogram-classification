import tensorflow as tf
from tensorflow.keras import backend as K
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.callbacks import TensorBoard
import pickle
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
NAME = "Benign-Malign-Normal-CNN"

class GalacticModelII:
    '''Default Model for Mammograph Classification'''
    def __init__(self):
        pass
    
    def architeture(self,x, default_steps, y):
        model = Sequential()
        X = x/255.0
        print(X.shape[1:])
        K.clear_session()
        model.add(Conv2D(32, (5, 5), input_shape=X.shape[1:]))
        model.add(Activation("relu"))
        model.add(Conv2D(64, (5, 5) , padding="same"))
        model.add(Activation("relu"))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Dropout(0.5))

        model.add(Flatten())
        model.add(Dense(1024))
        model.add(Activation("relu"))
        #model.add(Dropout(0.5))
        # softmax classifier
        model.add(Dense(2))
        model.add(Activation("softmax"))
        
        tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))
        model.compile(loss='sparse_categorical_crossentropy',
                    optimizer='adam',
                    metrics=['accuracy'])

        model.fit(X, y, batch_size=1, epochs=default_steps, validation_split=0.3, callbacks=[tensorboard])
        model.save('Mamogram.Model')
