#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 12:58:22 2018

@author: moritz
"""

from skmultiflow.data.file_stream import FileStream
from skmultiflow.classification.trees import HoeffdingTree
from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
from skmultiflow.evaluation.evaluate_holdout import EvaluateHoldout
import pandas as pd
from rslvq_stream import RSLVQ
from skmultiflow.classification.naive_bayes import NaiveBayes

"""init stream"""
stream = FileStream('datasets/electricity_final.csv', target_idx=-1, 
                    n_targets=1, cat_features_idx=[0, 2, 4, 6, 8])

stream = FileStream('datasets/gmsc_final.csv', target_idx=-1, 
                    n_targets=1)

stream.prepare_for_use()

"""init clf"""
clf = [HoeffdingTree(), RSLVQ(prototypes_per_class=8, gradient_descent='Adadelta', 
       sigma=0.01, decay_rate=0.999, learning_rate=0.001)]
"""eval stream"""
#evaluator = EvaluatePrequential(show_plot=True, # this will also slow down the process
#                                pretrain_size=1,
#                                max_samples=100000,
#                                metrics=['performance', 'kappa_t', 'kappa_m', 'kappa'],
#                                output_file=None)

evaluator = EvaluateHoldout(max_samples=1000000, batch_size=1, n_wait=10000, max_time=1000,
                                 output_file=None, show_plot=True, metrics=['performance',
                                                                            'kappa_t',
                                                                            'kappa_m',
                                                                            'kappa'],
                                 test_size=10000, dynamic_test_set=True)
#evaluator.evaluate(stream=stream, model=clf, model_names=['HTree', 'RSLVQ'])
evaluator.evaluate(stream=stream, model=clf)


# high decay rate needed for gmsc - adadelta; learning rate = 0.1 and higher for rmsprop