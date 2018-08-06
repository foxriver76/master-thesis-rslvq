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


X, y_true = make_blobs(n_samples=3000, centers=4,
                       cluster_std=1.0, random_state=None)
X = X[:, ::-1] # flip axes for better plotting

#stdizer = StandardScaler()
#X_std = stdizer.fit_transform(X=X)

t_new_start = time()
clf = RSLVQ(prototypes_per_class=4, gradient_descent='SGD', sigma=1.0)
labels_new = clf.partial_fit(X=X, y=y_true).predict(X)
t_new = time() - t_new_start

#t_old_start = time()
#clf = RslvqModel(prototypes_per_class=4, max_iter=1, sigma=1.0)
#labels_old = clf.fit(x=X, y=y_true).predict(X)
#t_old = time() - t_old_start

t_ada_start = time()
clf = RSLVQ(prototypes_per_class=4, gradient_descent='Adadelta', sigma=1.0, decay_rate=0.9)
labels_ada = clf.partial_fit(X=X, y=y_true).predict(X)
t_ada = time() - t_ada_start

acc_new = accuracy_score(y_true, labels_new)
acc_ada = accuracy_score(y_true, labels_ada)
#acc_old = accuracy_score(y_true, labels_old)


#print('Accuracy Old Model: {} \nAccuracy New Model: {}'.format(acc_old, acc_new))
#print('Time Old Model: {} \nTime New Model: {}'.format(t_old, t_new))

print('Accuracy Adadelta: {} \nAccuracy SGD: {}'.format(acc_ada, acc_new))
print('Time Adadelta: {} \nTime SGD: {}'.format(t_ada, t_new))

fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,11))

ax[0].scatter(X[:, 0], X[:, 1], c=labels_new, s=40, cmap='viridis')
ax[0].set_title('SGD')
ax[0].text(0.5, -0.1, 'Time: {} seconds\nAccuracy: {}'.format(t_new, acc_new), size=12, ha="center", 
         transform=ax[0].transAxes)

ax[1].scatter(X[:, 0], X[:, 1], c=labels_ada, s=40, cmap='viridis')
ax[1].set_title('Adadelta')
ax[1].text(0.5, -0.1, 'Time: {} seconds\nAccuracy: {}'.format(t_ada, acc_ada), size=12, ha="center", 
         transform=ax[1].transAxes)
plt.show()