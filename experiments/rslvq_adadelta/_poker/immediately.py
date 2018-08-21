#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 08:52:32 2018

@author: moritz
"""

from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
from skmultiflow.data.file_stream import FileStream
from rslvq_stream import RSLVQ
"""1. Create stream"""
stream = FileStream('../../../datasets/poker_final.csv', target_idx=-1, 
                    n_targets=1, cat_features_idx=[0, 2, 4, 6, 8])

stream.prepare_for_use()

"""2. Create classifier"""
clf = RSLVQ(prototypes_per_class=2, sigma=1.0, gradient_descent='Adadelta', decay_rate=0.9)

"""3. Setup evaluator"""
evaluator = EvaluatePrequential(show_plot=False,
                                pretrain_size=1,
                                max_samples=100000,
                                metrics=['performance', 'kappa_t', 'kappa_m', 'kappa'],
                                output_file=None)

"""4. Run evaluator"""
evaluator.evaluate(stream=stream, model=clf, model_names=['RSLVQ Ada'])