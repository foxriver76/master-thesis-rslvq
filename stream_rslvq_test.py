# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 08:26:04 2018

@author: moritz
"""

from skmultiflow.data.generators.waveform_generator import WaveformGenerator
from skmultiflow.data.generators.random_rbf_generator_drift import RandomRBFGeneratorDrift
from skmultiflow.data.generators.agrawal_generator import AGRAWALGenerator
from skmultiflow.data.generators.sea_generator import SEAGenerator
from skmultiflow.data.generators.sine_generator import SineGenerator
from skmultiflow.data.generators.mixed_generator import MIXEDGenerator
from skmultiflow.classification.trees.hoeffding_tree import HoeffdingTree
from skmultiflow.classification.trees.arf_hoeffding_tree import ARFHoeffdingTree
from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
from skmultiflow.evaluation.evaluate_holdout import EvaluateHoldout
from skmultiflow.evaluation.measure_collection import ClassificationMeasurements
from skmultiflow.classification.lazy.knn import KNN
from rslvq_stream import RSLVQ
from sklearn.linear_model import SGDClassifier
from skmultiflow.classification.naive_bayes import NaiveBayes

"""1. Create a stream"""
#stream = AGRAWALGenerator()
#stream = WaveformGenerator() # generate Stream 21 numeric attributes 3 classes
#stream = RandomRBFGeneratorDrift(sample_random_state = 50, 
#                                 n_classes = 2, n_features = 10, n_centroids = 50, 
#                                 change_speed=0.5, num_drift_centroids=50)
stream = SEAGenerator()
#stream = SineGenerator() # 500 iterations and 8 protos = 70.5 acc, pretrain=250 !sine has concept drift
stream.prepare_for_use() # prepare stream, has to be done before use

"""2. Instantiate the HoeffdingTree classifier"""
#clf = HoeffdingTree() # new classifier with default params
#clf = [RSLVQ(prototypes_per_class=1, max_iter=500), NaiveBayes()]
clf = RSLVQ(prototypes_per_class=1, max_iter=500)
#clf = NaiveBayes()
#clf = ARFHoeffdingTree()
#clf = KNN()

"""3. Setup the evaluator"""
#evaluator = EvaluatePrequential(show_plot=True, # this will also slow down the process
#                                pretrain_size=250,
#                                max_samples=40000,
#                                metrics=['performance', 'kappa', 'true_vs_predicts']) # eval parameter
evaluator = EvaluateHoldout(max_samples=40000, batch_size=200, n_wait=10000, max_time=1000,
                                 output_file=None, show_plot=True, metrics=['kappa', 
                                                                            'performance',
                                                                            'true_vs_predicts'],
                                 test_size=10000, dynamic_test_set=True)

"""4. Run evaluation"""
#evaluator.evaluate(stream=stream, model=clf, model_names=['RSLVQ', 'NaiveBayes']) #executes the eval process without it nothing happens
evaluator.evaluate(stream=stream, model=clf)
#Eval does the following things: Check if there are samples in the stream
#
#Pass the next sample to the classifier:
#
#        test the classifier (using predict())
#        update the classifier (using partial_fit())
#Update the evaluation results and plot
