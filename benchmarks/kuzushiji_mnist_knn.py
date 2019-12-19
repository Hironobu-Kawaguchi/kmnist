# kNN with neighbors=4 benchmark for Kuzushiji-MNIST
# Acheives 97.4% test accuracy

from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import os

def load(f):
    return np.load(f)['arr_0']

# Load the data
path = '../input'
x_train = load(os.path.join(path, 'kmnist-train-imgs.npz'))
x_test = load(os.path.join(path, 'kmnist-test-imgs.npz'))
y_train = load(os.path.join(path, 'kmnist-train-labels.npz'))
y_test = load(os.path.join(path, 'kmnist-test-labels.npz'))

# Flatten images
x_train = x_train.reshape(-1, 784)
x_test = x_test.reshape(-1, 784)

clf = KNeighborsClassifier(n_neighbors=4, weights='distance', n_jobs=-1)
print('Fitting', clf)
clf.fit(x_train, y_train)
print('Evaluating', clf)

test_score = clf.score(x_test, y_test)
print('Test accuracy:', test_score)
