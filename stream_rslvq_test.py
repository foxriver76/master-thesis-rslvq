# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 08:26:04 2018

@author: moritz
"""

from skmultiflow.data.generators.waveform_generator import WaveformGenerator
from skmultiflow.data.generators.random_rbf_generator_drift import RandomRBFGeneratorDrift
from skmultiflow.data.generators.agrawal_generator import AGRAWALGenerator
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
stream = WaveformGenerator() # generate Stream 21 numeric attributes 3 classes
#stream = RandomRBFGeneratorDrift(sample_random_state = 50, 
#                                 n_classes = 2, n_features = 10, n_centroids = 50, 
#                                 change_speed=0.5, num_drift_centroids=50)
stream.prepare_for_use() # prepare stream, has to be done before use

"""2. Instantiate the HoeffdingTree classifier"""
# ht = HoeffdingTree() # new classifier with default params
clf = RSLVQ(prototypes_per_class=4, max_iter=10)
#clf = NaiveBayes()
#clf = ARFHoeffdingTree()
#clf = HoeffdingTree(max_byte_size=633554432223, memory_estimate_period=2000000)
#clf = KNN()

"""3. Setup the evaluator"""
evaluator = EvaluatePrequential(show_plot=True, # this will also slow down the process
                                pretrain_size=500,
                                max_samples=5000,
                                metrics=['performance', 'kappa']) # eval parameter
#evaluator = EvaluateHoldout(max_samples=20000, batch_size=1, n_wait=10000, max_time=1000,
#                                 output_file=None, show_plot=True, metrics=['kappa', 'performance'],
#                                 test_size=5000, dynamic_test_set=True)

"""4. Run evaluation"""
evaluator.evaluate(stream=stream, model=clf) #executes the eval process without it nothing happens

#Eval does the following things: Check if there are samples in the stream
#
#Pass the next sample to the classifier:
#
#        test the classifier (using predict())
#        update the classifier (using partial_fit())
#Update the evaluation results and plot

print('correct classified labels: ', evaluator.global_classification_metrics[0].well_classified_labels)
print('incorrect classified labels: ', evaluator.global_classification_metrics[0].false_classified_labels)
print('All predicted labels: ', evaluator.global_classification_metrics[0].all_predicted_labels)