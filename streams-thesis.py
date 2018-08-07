#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 12:58:22 2018

@author: moritz
"""

from skmultiflow.data.file_stream import FileStream
from skmultiflow.classification.trees import HoeffdingTree
from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential

"""init stream"""
stream = FileStream(filepath='datasets/airlines.csv', target_idx=-1, 
                    n_targets=1, cat_features_idx=[1, 3, 4])

stream.prepare_for_use()

"""init clf"""
clf = HoeffdingTree()

"""eval stream"""
evaluator = EvaluatePrequential(show_plot=True, # this will also slow down the process
                                pretrain_size=1,
                                max_samples=50000,
                                metrics=['performance', 'kappa', 'true_vs_predicts'])

evaluator.evaluate(stream=stream, model=clf)