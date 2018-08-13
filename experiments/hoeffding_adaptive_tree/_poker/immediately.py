#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 08:52:32 2018

@author: moritz
"""

from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
from skmultiflow.data.file_stream import FileStream
from skmultiflow.classification.trees.hoeffding_adaptive_tree import HAT

"""1. Create stream"""
stream = FileStream('../../../datasets/poker_final.csv', target_idx=-1, 
                    n_targets=1, cat_features_idx=[0, 2, 4, 6, 8])

stream.prepare_for_use()

"""2. Create classifier"""
clf = HAT(split_criterion='info_gain')

"""3. Setup evaluator"""
evaluator = EvaluatePrequential(show_plot=False,
                                pretrain_size=1,
                                max_samples=100000,
                                metrics=['performance', 'kappa_t', 'kappa_m', 'kappa'],
                                output_file=None)

"""4. Run evaluator"""
evaluator.evaluate(stream=stream, model=clf, model_names=['HAT'])