# -*- coding: utf-8 -*-
"""
Created on Mon Jun 11 22:26:04 2018

@author: moritz
"""

from skmultiflow.data.generators.waveform_generator import WaveformGenerator
from skmultiflow.data.generators.random_rbf_generator_drift import RandomRBFGeneratorDrift
from skmultiflow.classification.trees.hoeffding_tree import HoeffdingTree
from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
from skmultiflow.classification.lazy.knn import KNN
#import matplotlib
#matplotlib.matplotlib_fname()
#matplotlib.use('Qt5Agg')
#matplotlib.use("Qt4Agg")
# type in console: 
#%matplotlib notebook

# 1. Create a stream
#stream = WaveformGenerator() # generate Stream 21 numeric attributes 3 classes
stream = RandomRBFGeneratorDrift(model_random_state=99, sample_random_state = 50, n_classes = 4, n_features = 10,
    n_centroids = 50, change_speed=0.87, num_drift_centroids=50)
stream.prepare_for_use() # prepare stream ?

# 2. Instantiate the HoeffdingTree classifier
ht = HoeffdingTree() # new classifier with default params

# 3. Setup the evaluator
evaluator = EvaluatePrequential(show_plot=True,
                                pretrain_size=200,
                                max_samples=25000) # eval parameter
# 4. Run evaluation
evaluator.evaluate(stream=stream, model=ht) #executes the eval process without it nothing happens

#Eval does the following things: Check if there are samples in the stream
#
#Pass the next sample to the classifier:
#
#        test the classifier (using predict())
#        update the classifier (using partial_fit())
#Update the evaluation results and plot