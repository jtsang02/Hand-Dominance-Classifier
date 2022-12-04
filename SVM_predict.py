import pickle
import numpy as np

filename = 'SVM_HandDominant_classifier.pkl'
Model = pickle.load(open(filename, 'rb'))

def predict(X):
    if Model.predict(X) == 1:
        return 'Dominant Hand'
    else:
        return 'Non-Dominant Hand'

if __name__ == "__main__":
    # random array of 31 features
    X = [[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1]]
    print(predict(X))
    Y = [[0.7, 0.2, 0.9, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1]]
    print(predict(Y))





