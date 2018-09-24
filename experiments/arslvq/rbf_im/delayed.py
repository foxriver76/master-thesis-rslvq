#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 08:53:06 2018

@author: moritz
"""
from skmultiflow.evaluation.evaluate_holdout import EvaluateHoldout
from skmultiflow.data.random_rbf_generator_drift import RandomRBFGeneratorDrift
from rslvq_stream import RSLVQ

"""1. Create stream"""
stream = RandomRBFGeneratorDrift(change_speed=0.0001)

stream.prepare_for_use()

"""2. Create classifier"""
clf = RSLVQ(gradient_descent='RMSprop', learning_rate=0.001, prototypes_per_class=1, sigma=3.0) # optimized

"""3. Setup evaluator"""
evaluator = EvaluateHoldout(max_samples=1000000, batch_size=1, n_wait=10000, max_time=1000,
                                 output_file=None, show_plot=False, metrics=['performance',
                                                                            'kappa_t',
                                                                            'kappa_m',
                                                                            'kappa'],
                                 test_size=10000, dynamic_test_set=True)


"""4. Run evaluator"""
evaluator.evaluate(stream=stream, model=clf, model_names=['RSLVQ RMSprop'])