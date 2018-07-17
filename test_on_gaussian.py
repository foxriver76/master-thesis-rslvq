#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  3 09:11:56 2018

@author: moritz
"""

from sklearn.datasets.samples_generator import make_blobs
import matplotlib.pyplot as plt
from rslvq_stream import RSLVQ
from sklearn.preprocessing import StandardScaler
from sklearn_lvq import RslvqModel


X, y_true = make_blobs(n_samples=400, centers=4,
                       cluster_std=0.60, random_state=None)
X = X[:, ::-1] # flip axes for better plotting

stdizer = StandardScaler()
X_std = stdizer.fit_transform(X=X)


clf = RSLVQ(gradient_descent='Adadelta', sigma=1.0)
labels = clf.partial_fit(X=X_std, y=y_true).predict(X)

#clf = RslvqModel(prototypes_per_class=4, max_iter=500)
#labels = clf.fit(x=X, y=y_true).predict(X)

plt.scatter(X[:, 0], X[:, 1], c=labels, s=40, cmap='viridis')
plt.show()