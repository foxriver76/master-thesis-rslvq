#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 12:58:22 2018

@author: moritz
"""

from skmultiflow.data.file_stream import FileStream
from skmultiflow.classification.trees import HoeffdingTree
from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
import pandas as pd
from rslvq_stream import RSLVQ

"""init stream"""
#stream = FileStream('datasets/electricity_final.csv', target_idx=-1, 
#                    n_targets=1, cat_features_idx=[0, 2, 4, 6, 8])

stream = FileStream('datasets/gmsc_final.csv', target_idx=-1, 
                    n_targets=1)

stream.prepare_for_use()

"""init clf"""
clf = [HoeffdingTree(), RSLVQ(prototypes_per_class=8, gradient_descent='RMSprop')]

"""eval stream"""
evaluator = EvaluatePrequential(show_plot=True, # this will also slow down the process
                                pretrain_size=1,
                                max_samples=100000,
                                metrics=['performance', 'kappa_t'],
                                output_file=None)

evaluator.evaluate(stream=stream, model=clf, model_names=['HTree', 'RSLVQ'])