#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 09:11:56 2018

@author: moritz
"""

from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from rslvq_stream import RSLVQ
#from sklearn.preprocessing import StandardScaler
from sklearn_lvq import RslvqModel
from sklearn.metrics import accuracy_score
from time import time


X, y_true = make_blobs(n_samples=9000, centers=4,
                       cluster_std=1.0, random_state=None)
X = X[:, ::-1] # flip axes for better plotting

#stdizer = StandardScaler()
#X_std = stdizer.fit_transform(X=X)

t_new_start = time()
clf = RSLVQ(prototypes_per_class=4, gradient_descent='SGD', sigma=1.0)
labels_new = clf.partial_fit(X=X, y=y_true).predict(X)
t_new = time() - t_new_start

t_old_start = time()
clf = RslvqModel(prototypes_per_class=4, max_iter=1, sigma=1.0)
labels_old = clf.fit(x=X, y=y_true).predict(X)
t_old = time() - t_old_start

acc_new = accuracy_score(y_true, labels_new)
acc_old = accuracy_score(y_true, labels_old)


print('Accuracy Old Model: {} \nAccuracy New Model: {}'.format(acc_old, acc_new))
print('Time Old Model: {} \nTime New Model: {}'.format(t_old, t_new))

plt.scatter(X[:, 0], X[:, 1], c=labels_new, s=40, cmap='viridis')
plt.show()