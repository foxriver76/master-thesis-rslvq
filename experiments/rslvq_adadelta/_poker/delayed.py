#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 08:53:06 2018

@author: moritz
"""
from skmultiflow.evaluation.evaluate_holdout import EvaluateHoldout
from skmultiflow.data.file_stream import FileStream
from rslvq_stream import RSLVQ
"""1. Create stream"""
stream = FileStream('../../../datasets/poker_final.csv', target_idx=-1,
                    cat_features_idx=[0,2,4,6,8])

stream.prepare_for_use()

"""2. Create classifier"""
clf = RSLVQ(prototypes_per_class=1, sigma=1.0, gradient_descent='Adadelta', decay_rate=1.0) # optimized + manual

"""3. Setup evaluator"""
evaluator = EvaluateHoldout(max_samples=1000000, batch_size=1, n_wait=10000, max_time=1000,
                                 output_file=None, show_plot=False, metrics=['performance',
                                                                            'kappa_t',
                                                                            'kappa_m',
                                                                            'kappa'],
                                 test_size=10000, dynamic_test_set=True)

"""4. Run evaluator"""
evaluator.evaluate(stream=stream, model=clf, model_names=['RSLVQ Ada'])