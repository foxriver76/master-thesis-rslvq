#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 08:52:32 2018

@author: moritz
"""

from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
from skmultiflow.data.random_rbf_generator_drift import RandomRBFGeneratorDrift
from rslvq_stream import RSLVQ

"""1. Create stream"""
stream = RandomRBFGeneratorDrift(change_speed=0.0001)

stream.prepare_for_use()

"""2. Create classifier"""
clf = RSLVQ(gradient_descent='RMSprop', learning_rate=0.001, prototypes_per_class=1, sigma=3.0) # optimized

"""3. Setup evaluator"""
evaluator = EvaluatePrequential(show_plot=False,
                                pretrain_size=1,
                                max_samples=1000000,
                                metrics=['performance', 'kappa_t', 'kappa_m', 'kappa'],
                                output_file=None)

"""4. Run evaluator"""
evaluator.evaluate(stream=stream, model=clf, model_names=['RSLVQ RMSprop'])