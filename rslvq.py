#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 20 14:55:50 2018

@author: moritz
"""

from sklearn_lvq import RslvqModel
from sklearn import datasets
from sklearn.metrics import accuracy_score

"""Import data"""
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target

clf = RslvqModel()
clf.fit(X, y)

y_pred = clf.predict(X)

"""Model evaluation"""
accuracy = accuracy_score(y_true=y, y_pred=y_pred)
print('Accuracy Score: %.3f' % accuracy)
