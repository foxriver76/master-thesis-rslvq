# -*- coding: utf-8 -*-

from skmultiflow.data.generators.waveform_generator import WaveformGenerator
from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
from skmultiflow.classification.naive_bayes import NaiveBayes

stream = WaveformGenerator()

stream.prepare_for_use() 

clf = NaiveBayes()

evaluator = EvaluatePrequential(show_plot=True, 
                                pretrain_size=500,
                                max_samples=50000,
                                metrics=['performance', 'kappa']) 

evaluator.evaluate(stream=stream, model=clf)