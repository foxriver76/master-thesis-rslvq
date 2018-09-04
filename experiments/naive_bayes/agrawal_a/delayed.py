#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 08:53:06 2018

@author: moritz
"""
from skmultiflow.evaluation.evaluate_holdout import EvaluateHoldout
from skmultiflow.bayes.naive_bayes import NaiveBayes
from skmultiflow.data.concept_drift_stream import ConceptDriftStream
from skmultiflow.data import AGRAWALGenerator

"""1. Create stream"""
stream = ConceptDriftStream(stream=AGRAWALGenerator(random_state=112), 
                            drift_stream=AGRAWALGenerator(random_state=112, classification_function=2),
                            random_state=None,
                            alpha=90.0, # angle of change grade 0 - 90, overwrites width
                            position=250000,
                            width=1)

stream.prepare_for_use()

"""2. Create classifier"""
clf = NaiveBayes()

"""3. Setup evaluator"""
evaluator = EvaluateHoldout(max_samples=1000000, batch_size=1, n_wait=10000, max_time=1000,
                                 output_file=None, 
                                 show_plot=False, 
                                 metrics=['performance',
                                            'kappa_t',
                                            'kappa_m',
                                            'kappa'],
                                 test_size=10000, dynamic_test_set=True)


"""4. Run evaluator"""
evaluator.evaluate(stream=stream, model=clf, model_names=['HAT'])