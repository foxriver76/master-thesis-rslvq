#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 08:52:32 2018

@author: moritz
"""

from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
from skmultiflow.data.concept_drift_stream import ConceptDriftStream
from skmultiflow.data import AGRAWALGenerator
from skmultiflow.trees.hoeffding_adaptive_tree import HAT

"""1. Create stream"""
stream = ConceptDriftStream(stream=AGRAWALGenerator(random_state=112, perturbation=0.1), 
                            drift_stream=AGRAWALGenerator(random_state=112, 
                                                          classification_function=2, perturbation=0.1),
                            random_state=None,
                            position=250000,
                            width=50000)
stream.prepare_for_use()

"""2. Create classifier"""
clf = HAT(split_criterion='info_gain')

"""3. Setup evaluator"""
evaluator = EvaluatePrequential(show_plot=False,
                                pretrain_size=1,
                                max_samples=1000000,
                                metrics=['performance', 'kappa_t', 'kappa_m', 'kappa'],
                                output_file=None)

"""4. Run evaluator"""
evaluator.evaluate(stream=stream, model=clf, model_names=['HAT'])