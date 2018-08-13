# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 08:26:04 2018

@author: moritz
"""

from skmultiflow.data.generators.waveform_generator import WaveformGenerator
from skmultiflow.data.generators.random_rbf_generator_drift import RandomRBFGeneratorDrift
from skmultiflow.data.generators.random_rbf_generator import RandomRBFGenerator
from skmultiflow.data.generators.agrawal_generator import AGRAWALGenerator
from skmultiflow.data.generators.sea_generator import SEAGenerator
from skmultiflow.data.generators.sine_generator import SineGenerator
from skmultiflow.data.generators.mixed_generator import MIXEDGenerator
from skmultiflow.classification.trees.hoeffding_tree import HoeffdingTree
from skmultiflow.classification.trees.arf_hoeffding_tree import ARFHoeffdingTree
from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
from skmultiflow.evaluation.evaluate_holdout import EvaluateHoldout
from skmultiflow.evaluation.measure_collection import ClassificationMeasurements
from skmultiflow.classification.lazy.sam_knn import SAMKNN
from skmultiflow.classification.lazy.knn import KNN
from rslvq_stream import RSLVQ
from skmultiflow.classification.naive_bayes import NaiveBayes
from sklearn.linear_model import SGDClassifier
from skmultiflow.data.generators.hyper_plane_generator import HyperplaneGenerator

"""1. Create a stream"""
#stream = HyperplaneGenerator(random_state=None, n_features=10, n_drift_features=2, 
#                                                                      mag_change=0.0, 
#                                                                      noise_percentage=0.05, 
#                                                                      sigma_percentage=0.1)
#stream = AGRAWALGenerator()
#stream = WaveformGenerator(has_noise=True) # generate Stream 21 numeric attributes 3 classes
#stream = RandomRBFGeneratorDrift(sample_random_state = 50, 
#                                 n_classes = 2, n_features = 10, n_centroids = 50, 
#                                 change_speed=0.5, num_drift_centroids=50)
#stream = RandomRBFGenerator(model_random_state=None, sample_random_state=None, n_classes=2, 
#                                                                    n_features=10, 
#                                                                    n_centroids=50)

#stream = SEAGenerator()
stream = SineGenerator() # 500 iterations and 8 protos = 70.5 acc, pretrain=250 !sine has concept drift
stream.prepare_for_use() # prepare stream, has to be done before use

"""2. Instantiate the HoeffdingTree classifier"""
clf = HoeffdingTree() # new classifier with default params
#clf = [RSLVQ(prototypes_per_class=2, max_iter=500, gradient_descent='l-bfgs-b', sigma=3.0), 
#       RSLVQ(prototypes_per_class=2, max_iter=500, gradient_descent='SGD', sigma=3.0)]
#clf = RSLVQ(prototypes_per_class=1, sigma=3.0)
#clf = NaiveBayes()
#clf = ARFHoeffdingTree()
#clf = KNN()
#clf = [RSLVQ(prototypes_per_class=2, max_iter=300, gradient_descent='SGD', sigma=1.0), 
#       RSLVQ(prototypes_per_class=2, max_iter=300, gradient_descent='Adadelta', decay_rate=0.9, sigma=1.0),
#       RSLVQ(prototypes_per_class=2, max_iter=300, gradient_descent='RMSprop', \
#             learning_rate=0.001, sigma=1.0)]
#       HoeffdingTree(),
#       ARFHoeffdingTree(),
#       SAMKNN(n_neighbors=5, knnWeights='distance')]

#clf = RSLVQ(prototypes_per_class=10, max_iter=300, gradient_descent='RMSprop',
#             learning_rate=0.001, decay_rate=0.9, sigma=1.0)

"""3. Setup the evaluator"""
evaluator = EvaluatePrequential(show_plot=True, # this will also slow down the process
                                pretrain_size=1,
                                max_samples=60000,
                                metrics=['performance', 'kappa', 'true_vs_predicts']) # eval parameter
#evaluator = EvaluateHoldout(max_samples=1500000, batch_size=1, n_wait=10000, max_time=1000,
#                                 output_file=None, show_plot=True, metrics=['kappa', 
#                                                                            'performance',
#                                                                            'true_vs_predicts'],
#                                 test_size=10000, dynamic_test_set=True)

"""4. Run evaluation"""
#evaluator.evaluate(stream=stream, model=clf, model_names=['RSLVQalt', 'RSLVQneu']) #executes the eval process without it nothing happens
evaluator.evaluate(stream=stream, model=clf)
#evaluator.evaluate(stream=stream, model=clf, model_names=['SGD', 'Adadelta', 
#                                                          'RMSprop']) #, 'HTree', 
#                                                          #'AHTree', 'SAMKNN'])

#Eval does the following things: Check if there are samples in the stream
#
#Pass the next sample to the classifier:
#
#        test the classifier (using predict())
#        update the classifier (using partial_fit())
#Update the evaluation results and plot