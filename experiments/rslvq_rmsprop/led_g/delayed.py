#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 08:53:06 2018

@author: moritz
"""
from skmultiflow.evaluation.evaluate_holdout import EvaluateHoldout
from skmultiflow.data.led_generator_drift import LEDGeneratorDrift
from rslvq_stream import RSLVQ
from skmultiflow.data.concept_drift_stream import ConceptDriftStream

"""1. Create stream"""
stream = ConceptDriftStream(stream=LEDGeneratorDrift(has_noise=False, noise_percentage=0.0, n_drift_features=3),
                            drift_stream=LEDGeneratorDrift(has_noise=False, noise_percentage=0.0, n_drift_features=7),
                            random_state=None,
                            position=250000,
                            width=50000)

stream.prepare_for_use()

"""2. Create classifier"""
clf = RSLVQ(gradient_descent='RMSprop', sigma=1.0, prototypes_per_class=1) #optimized

"""3. Setup evaluator"""
evaluator = EvaluateHoldout(max_samples=1000000, batch_size=1, n_wait=10000, max_time=1000,
                                 output_file=None, show_plot=False, metrics=['performance',
                                                                            'kappa_t',
                                                                            'kappa_m',
                                                                            'kappa'],
                                 test_size=10000, dynamic_test_set=True)


"""4. Run evaluator"""
evaluator.evaluate(stream=stream, model=clf, model_names=['HAT'])