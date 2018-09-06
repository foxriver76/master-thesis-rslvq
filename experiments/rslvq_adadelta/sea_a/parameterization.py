#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 08:34:18 2018

@author: moritz
"""

from sklearn.model_selection import GridSearchCV
from rslvq_stream import RSLVQ
import json
from skmultiflow.data.concept_drift_stream import ConceptDriftStream
from skmultiflow.data import SEAGenerator

"""Subset of 30k"""
stream = ConceptDriftStream(stream=SEAGenerator(random_state=112, noise_percentage=0.1), 
                            drift_stream=SEAGenerator(random_state=112, 
                                                          classification_function=2, noise_percentage=0.1),
                            alpha=90.0,
                            random_state=None,
                            position=250000,
                            width=1)

stream.prepare_for_use()

X, y = stream.next_sample(batch_size=30000)

clf = RSLVQ()

"""Specify possible params"""
ppt_range = [1, 2, 4, 8, 10, 12]
sigma_range = [1.0, 2.0, 3.0, 5.0]
decay_range = [0.9, 0.7, 0.5, 0.3, 0.1, 0.001]



param_grid = [{'sigma': sigma_range,
               'gradient_descent': ['Adadelta'],
               'prototypes_per_class': ppt_range,
                'decay_rate': decay_range}]

gs = GridSearchCV(estimator=clf,
                  param_grid=param_grid,
                  scoring='accuracy',
                  cv=10,
                  n_jobs=-1)

gs = gs.fit(X, y)

"""Print best params"""
print(gs.best_score_)
print(gs.best_params_)

"""Test classifier"""
clf = gs.best_estimator_

clf.fit(X, y)

print('Korrektklassifizierungsraten: \
    %.3f' % clf.score(X, y))

accuracy = clf.score(X, y) 

"""Write results to File"""
file = open('../../param_search_results.txt', 'a+')

file.write(50 * '-')
file.write('\nSEA- RSLVQ SGD\n')
file.write('\nBest score: %.5f ' % (gs.best_score_))
file.write('\nBest param: %s' % (json.dumps(gs.best_params_)))
file.write('\nTest Accuracy: %.5f \n\n' % (accuracy))

file.close()