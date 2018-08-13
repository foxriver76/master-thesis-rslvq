#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 08:53:06 2018

@author: moritz
"""
from skmultiflow.evaluation.evaluate_holdout import EvaluateHoldout
from skmultiflow.data.file_stream import FileStream
from skmultiflow.classification.trees.hoeffding_adaptive_tree import HAT

"""1. Create stream"""
stream = FileStream('../../../datasets/gmsc_final.csv', target_idx=-1)

stream.prepare_for_use()

"""2. Create classifier"""
clf = HAT(split_criterion='info_gain')

"""3. Setup evaluator"""
evaluator = EvaluateHoldout(max_samples=1000000, batch_size=1, n_wait=10000, max_time=1000,
                                 output_file=None, show_plot=False, metrics=['performance',
                                                                            'kappa_t',
                                                                            'kappa_m',
                                                                            'kappa'],
                                 test_size=10000, dynamic_test_set=True)


"""4. Run evaluator"""
evaluator.evaluate(stream=stream, model=clf, model_names=['HAT'])