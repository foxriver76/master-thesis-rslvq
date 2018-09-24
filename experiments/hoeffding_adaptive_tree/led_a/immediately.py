#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 08:52:32 2018

@author: moritz
"""

from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
from skmultiflow.data.led_generator_drift import LEDGeneratorDrift
from skmultiflow.trees.hoeffding_adaptive_tree import HAT
from skmultiflow.data.concept_drift_stream import ConceptDriftStream

"""1. Create stream"""
stream = ConceptDriftStream(stream=LEDGeneratorDrift(has_noise=False, noise_percentage=0.0, n_drift_features=3),
                            drift_stream=LEDGeneratorDrift(has_noise=False, noise_percentage=0.0, n_drift_features=7),
                            random_state=None,
                            alpha=90.0, # angle of change grade 0 - 90
                            position=250000,
                            width=1)

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