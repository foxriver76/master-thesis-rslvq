#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 12:58:22 2018

@author: moritz
"""

from skmultiflow.data.file_stream import FileStream
from skmultiflow.data.random_rbf_generator_drift import RandomRBFGeneratorDrift
from skmultiflow.data.agrawal_generator import AGRAWALGenerator
from skmultiflow.data.random_tree_generator import RandomTreeGenerator
from skmultiflow.data.hyper_plane_generator import HyperplaneGenerator
from skmultiflow.data.sea_generator import SEAGenerator
from skmultiflow.data.concept_drift_stream import ConceptDriftStream
from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
from rslvq_stream import RSLVQ
from adrslvq import ARSLVQ

"""init stream"""
#stream = FileStream('datasets/poker_final.csv', target_idx=-1,
#                    n_targets=1, cat_features_idx=[0, 2, 4, 6, 8])
#stream = AGRAWALGenerator()
#stream = ConceptDriftStream(stream=SEAGenerator(classification_function=0), 
#                            drift_stream=SEAGenerator(classification_function=2),
#                            position=0,
#                            width=50000)
stream = HyperplaneGenerator(mag_change=0.5, n_drift_features=5, sigma_percentage=0.5)
#stream = RandomTreeGenerator()
#stream = FileStream('datasets/electricity_final.csv', target_idx=-1)
#stream = RandomRBFGeneratorDrift(change_speed=0.3)


stream.prepare_for_use()

"""init clf"""
clf = [ARSLVQ(prototypes_per_class=1, sigma=1.0, learning_rate=0.01), 
       RSLVQ(gradient_descent='Adadelta', learning_rate=0.001, sigma=1.0, decay_rate=0.999)]

"""eval stream"""
#evaluator = EvaluatePrequential(show_plot=True, # this will also slow down the process
#                                pretrain_size=1,
#                                max_samples=100000,
#                                metrics=['performance', 'kappa_t', 'kappa_m', 'kappa'],
#                                output_file=None)

evaluator = EvaluatePrequential(max_samples=1000000, batch_size=1,
                                 output_file=None, pretrain_size=1, show_plot=True, 
                                 metrics=['performance',
                                            'kappa_t',
                                            'kappa_m',
                                            'kappa'])

evaluator.evaluate(stream=stream, model=clf, model_names=['ARSLVQ', 'RSLVQ'])
