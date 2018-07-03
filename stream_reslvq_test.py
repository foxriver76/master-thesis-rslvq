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
from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
from skmultiflow.classification.lazy.knn import KNN
from rslvq_stream import RslvqStreamModel
from sklearn.linear_model import SGDClassifier
#import matplotlib
#matplotlib.matplotlib_fname()
#matplotlib.use('Qt5Agg')
#matplotlib.use("Qt4Agg")
# type in console: 
#%matplotlib notebook

# 1. Create a stream
#stream = AGRAWALGenerator()
#stream = WaveformGenerator() # generate Stream 21 numeric attributes 3 classes
stream = RandomRBFGeneratorDrift(sample_random_state = 50, 
                                 n_classes = 2, n_features = 10, n_centroids = 50, 
                                 change_speed=0.5, num_drift_centroids=50)
stream.prepare_for_use() # prepare stream, has to be done before use

# 2. Instantiate the HoeffdingTree classifier
# ht = HoeffdingTree() # new classifier with default params
clf = RslvqStreamModel()
#clf = HoeffdingTree()
#clf = KNN()

# 3. Setup the evaluator
evaluator = EvaluatePrequential(show_plot=True,
                                pretrain_size=500,
                                max_samples=5000) # eval parameter
# 4. Run evaluation
evaluator.evaluate(stream=stream, model=clf) #executes the eval process without it nothing happens

#Eval does the following things: Check if there are samples in the stream
#
#Pass the next sample to the classifier:
#
#        test the classifier (using predict())
#        update the classifier (using partial_fit())
#Update the evaluation results and plot