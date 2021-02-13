from tensorflow.keras.models import load_model, save_model
from featurizer import extract
from keras.callbacks import EarlyStopping
from os import pardir
import numpy as np

def retrain():
    '''
    Retrain the LSTM
    '''

    X = []
    Y = []

    f = open("assets/data/name_gender.csv")
    data = f.readlines()
    f.close()
    for line in data:
        name, gender = line.split(',')
        if name and gender:
            tensor = extract(name)
            if type(tensor) == np.ndarray:
                X.extend(tensor.tolist())
            Y.append([1, 0] if gender.strip("\n") == 'M' else [0, 1])

    X = np.array(X)
    Y = np.array(Y)

    if X.shape[0] > 0 and Y.shape[0] > 0:
        callback = EarlyStopping(
            monitor='val_loss', min_delta=0, patience=3, verbose=0,
            mode='auto', baseline=None, restore_best_weights=True
        )

        model = load_model("assets/model/LSTMSimple")
        model.fit(X, Y, batch_size=1, epochs=X.shape[0], validation_data=(X, Y),
                            callbacks=[callback])
        save_model(model, "assets/model/LSTMSimple", save_format="h5")

#if __name__ == '__main__':
#    retrain()