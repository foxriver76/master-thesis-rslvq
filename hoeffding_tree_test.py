# -*- coding: utf-8 -*-

from skmultiflow.data.generators.waveform_generator import WaveformGenerator
from skmultiflow.data.generators.sea_generator import SEAGenerator
from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
from skmultiflow.classification.trees.hoeffding_tree import HoeffdingTree

#stream = WaveformGenerator()
stream = SEAGenerator()

stream.prepare_for_use() 

clf = HoeffdingTree()

evaluator = EvaluatePrequential(show_plot=True, 
                                pretrain_size=250,
                                max_samples=50000,
                                metrics=['performance', 'kappa']) 

evaluator.evaluate(stream=stream, model=clf)