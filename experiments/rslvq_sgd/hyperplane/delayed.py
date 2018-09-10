#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 08:53:06 2018

@author: moritz
"""
from skmultiflow.evaluation.evaluate_holdout import EvaluateHoldout
from skmultiflow.data.hyper_plane_generator import HyperplaneGenerator
from rslvq_stream import RSLVQ

"""1. Create stream"""
stream = HyperplaneGenerator(mag_change=0.001, noise_percentage=0.1)

stream.prepare_for_use()

"""2. Create classifier"""
clf = RSLVQ(prototypes_per_class=1, sigma=1.0, gradient_descent='SGD') # optimized

"""3. Setup evaluator"""
evaluator = EvaluateHoldout(max_samples=1000000, batch_size=1, n_wait=10000, max_time=1000,
                                 output_file=None, show_plot=False, metrics=['performance',
                                                                            'kappa_t',
                                                                            'kappa_m',
                                                                            'kappa'],
                                 test_size=10000, dynamic_test_set=True)


"""4. Run evaluator"""
evaluator.evaluate(stream=stream, model=clf, model_names=['HAT'])