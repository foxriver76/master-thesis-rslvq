#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 11:18:24 2018

@author: Moritz Heusinger <moritz.heusinger@gmail.com>
"""


#from scipy.stats.mstats import friedmanchisquare as Friedman
from lib import friedman_test as Friedman, bonferroni_dunn_test as Bon_dunn
import datetime
import numpy as np

#######################################
#                                     #
#              How-To                 #
#                                     #
#######################################

"""
Provide the names of your algorithms as a list of strings, e.g. like

algorithm_names = ['RSLVQ SGD',
                   'RSLVQ ADA',
                   'RSLVQ RMS',
                   'Naive Bayes',
                   'Hoeffding Tree',
                   'Adaptive Hoeffding Tree'
                    ]

Provide the accuracy scores of your algorithm as a 2D list. Every list represents 
one algorithm. Every scalar (float) of the list represents the accuracy score for one 
problem. E.g.

accuracys_per_algorithm = [[85.3, 71.5, 74.7], 
                         [85.3, 93.1, 75.1], 
                         [85.3, 85.8, 74.8],
                         [58.0, 14.8, 38.9],
                         [80.9, 93.2, 71.2],
                         [88.3, 88.1, 71.3]]
 
Thus, every algorithm contains three accuracy scores and five algorithms are compared.

At the end you have to define which algorithm should be compared by the Bon Dunn Test.
For this, pass a single string to a variable called 'comparing_algorithm'. E.g.

comparing_algorithm = 'RSLVQ ADA'

Optional:
    
You can set a path to the output file by setting the write_to_file variable. E.g. 

write_to_file = 'statistic_test_result.txt'

if 'write_to_file = None'. No output file is written. The output file contains 
the results as well as the datetime. 

"""

#######################################
#                                     #
#              Inputs                 #
#                                     #
#######################################

algorithm_names = ['ARSLVQ',
                    'RSLVQ SGD',
                   'RSLVQ ADA',
                   'RSLVQ RMS',
                   'Naive Bayes',
                   'Hoeffding Tree',
                   'Adaptive Hoeffding Tree'
                    ]
### Immediate accuracy
#accuracys_per_algorithm = [
#        [99.9,67.2,99.6,99.9,100,100,100],
#        [99.9,67.1,99.8,100,100,100,99.9],
#        [90.0,82.9,88.7,89.9,71.6,90.0,83.9],
#        [89.9,82.2,88.9,89.9,67.7,89.6,83.2],
#        [51.2,50.1,54.3,51.5,50.8,99.9,79.8],
#        [53.6,52.7,53.3,53.3,55.5,86.7,79.3],
#        [64.8,58.8,68.5,62.3,73.1,84.0,60.5],
#        [56.2,59.7,59.8,52.5,50,59.8,68.8],
#        [62.1,53.8,57.6,59.5,50,68.1,74.4],
#        [84.1,56.7,87.3,86.1,73.6,80.3,84.9],
#        [75.2,63.1,75.8,74.5,74.0,85.8,81.5],
#        [3.6,6.4,4.0,3.6,4.1,1.8,2.7],
#        [85.3,85.3,85.3,85.3,58.0,80.9,88.3],
#        [86.5,71.5,93.1,85.8,14.8,93.2,88.1],
#        [73.4,74.7,75.1,74.8,38.9,71.2,71.3],
#        [81.7,77.2,84.5,82.0,37.2,81.8,82.6],
#        [3.3,3.7,1.7,3.0,7.0,4.3,3.0],
#        [76.7,66.4,77.8,76.2,64.0,84.9,81.7],
#        [3.5,5.8,3.5,3.5,5.7,2.4,2.8]
#]

### Immediate Kappa
#accuracys_per_algorithm = [
#        [99.9, 63.5, 99.6, 99.9, 100, 100, 99.9],
#        [99.8, 63.4, 99.8, 100, 100, 100, 99.9],
#        [75.5, 59.0, 72.6, 75.1, 29.9, 75.6, 60.7],
#        [78.9, 62.8, 76.8, 78.8, 30.5, 78.2, 64.9],
#        [0.1, 0.3, -0.1, 1.4, 0.3, 99.9, 58.6],
#        [6.4, 4.1, 5.9, 6.0, 10.6, 73.3, 57.6],
#        [26.4, 17.3, 31.5, 23.8, 36.2, 66.0, 20.7],
#        [0.1, 15.6, 15.4, 4.4, 5.0, 13.0, 24.1],
#        [7.7, 6.3, 14.0, 17.0, 5.0, 35.9, 43.2],
#        [68.2, 13.5, 74.6, 72.2, 47.1, 60.6, 69.8],
#        [46.3, 30.6, 49.0, 47.9, 44.3, 70.3, 59.9], 
#        [4.1, 5.9, 4.4, 3.3, 4.0, 2.0, 2.8], 
#        [70.0, 70.0, 70.0, 70.0, 6.3, 60.8, 76.0], 
#        [0.2, -0.4, 0.0, -1.1, 0.5, 19.3, 1.2], 
#        [53.5, 55.0, 56.2, 55.3, 6.1, 47.5, 49.0], 
#        [41.2, 41.5, 42.1, 41.4, 4.3, 42.5, 42.1], 
#        [3.3, 4.0, 2.7, 3.3, 5.7, 4.3, 2.7], 
#        [45.1, 33.1, 47.4, 46.4, 33.4, 63.9, 55.8], 
#        [3.9, 5.5, 4, 3.3, 4.5, 2.5, 2.8]
#]

### Immediate Kappa T
#accuracys_per_algorithm = [
#    [99.9, 63.5, 99.6, 99.9, 100, 100, 99.9],
#    [99.8, 63.4, 99.8, 100, 100, 100, 99.9],
#    [76.4, 59.6, 73.3, 76.0, 33.0, 76.3, 61.9],
#    [79.0, 62.8, 76.8, 78.8, 32.5, 78.4, 65.0],
#    [-0.9, -3.3, 5.4, -0.3, -1.8, 99.9, 58.2],
#    [0.4, -1.5, -0.1, -0.1, 4.6, 71.5, 57.2],
#    [27.6, 17.6, 34.1, 24.2, 41.1, 66.3, 20.5],
#    [11.0, 17.7, 17.8, 5.1, 5, 17.6, 30.3],
#    [20.0, 5.9, 14.5, 18.2, 5, 35.9, 45.4],
#    [68.2, 13.6, 74.6, 72.2, 47.1, 60.6, 69.8],
#    [48.1, 29.9, 49.6, 47.4, 44.6, 70.7, 60.8],
#    [3.5, 6.3, 3.8, 3.5, 4.1, 2.1, 3.2],
#    [0.0, 0.0, 0.0, 0.0, -186.3, -30.4, 20.0],
#    [-0.5, -121.1, 46.0, -10.3, -561.2, 47.1, 7.0],
#    [-4.3, 0.6, 2.3, 0.9, -139.9, -13.0, -12.6],
#    [-1.6, -40.2, 16.1, -3.1, -289.8, 1.2, 4.8],
#    [3.3, 3.7, 1.7, 3.0, 7.0, 4.3, 3.0],
#    [36.7, 13.8, 41.9, 35.7, -48.3, 54.6, 47.9],
#    [3.5, 5.7, 3.3, 3.4, 4.9, 2.6, 3.2]
#]

accuracys_per_algorithm = [
        [99.9, 63.5, 99.6, 99.9, 100, 100, 99.9],
        [99.8, 63.4, 99.8, 100, 100, 100, 99.9],
        [85.6, 75.4, 83.7, 85.4, 59.2, 85.5, 76.8],
        [83.1, 70.1, 81.3, 83.0, 45.7, 82.6, 71.9],
        [-13.5, -16.2, -6.0, -12.8, -14.1, 99.9, 52.9],
        [-1.6, -3.5, -2.1, -2.2, 2.6, 71.0, 51.8],
        [39.9, 14.2, 48.0, 18.5, 24.1, 58.6, 15.5],
        [0.00, 5.7, 6.1, 7.6, 5, 30.8, 7.9],
        [1.6, -6.0, 7.2, 11.5, 5, 32.4, 59.3],
        [68.1, 13.4, 74.6, 72.2, 47.0, 60.5, 69.8],
        [46.3, 28.0, 49.2, 46.3, 45.6, 72.1, 60.6],
        [3.7, 6.5, 3.8, 3.2, 4.4, 1.8, 3.3],
        [65.4, 65.4, 65.4, 65.4, 1.0, 54.9, 72.3],
        [-94.6, -309.8, 0, -104.4, -1125.7, 2.0, -72.6],
        [72.5, 73.8, 74.2, 73.8, 36.7, 52.6, 70.3],
        [14.4, -56.9, 46.5, 11.6, -362.7, 36.5, 23.3],
        [3.3, 3.3, 1.7, 3.0, 7.0, 4.3, 3.0],
        [38.9, 8.4, 48.6, 38.3, -65.8, 63.9, 52.0],
        [3.6, 5.8, 3.3, 3.2, 5.1, 2.4, 3.2]
    ]

accuracys_per_algorithm = np.asarray(accuracys_per_algorithm).T

write_to_file = 'statistic_test_result.txt'

#######################################
#                                     #
#            Calculations             #
#                                     #
#######################################

f_value, p_value, rankings, pivots = Friedman(*accuracys_per_algorithm)

pivot_dict = dict(zip(algorithm_names, pivots))

if(p_value < 0.05):
    fried_sig_string = 'Significant'
#    print('Friedman: Significant :)')
else: 
    fried_sig_string = 'Not significant'
#    print('Friedman: Not significant :(')
    
comparsions_res = []
p_res = []
z_res = []
comp_length = []

for i in range(len(algorithm_names)):
    comparing_algorithm = algorithm_names[i]

    comparsions, z_values, p_values, adj_p_values = Bon_dunn(ranks=pivot_dict, control=comparing_algorithm)
    
    comparsions_res.append(comparsions)
    p_res.append(p_values)
    z_res.append(z_values)
    
    # max length calc for file formatting
    [comp_length.append(len(comparsions_res[i][j])) for j in range(len(comparsions_res[i]))]
    
max_len = max(comp_length)

#######################################
#                                     #
#            Write File               #
#                                     #
#######################################

if(write_to_file):
    file = open(write_to_file, 'a+')
    time = datetime.datetime.now()
    file.write(50 * '-')
    file.write('\n%s' % (str(time)))
    file.write('\nCompared algorithms: %s' % (str(algorithm_names)))
    file.write('\nFriedman p-value: %.8f --> %s' % (p_value, fried_sig_string))
    file.write('\n\n')
    file.write('Bonferroni Dunn Test: \n')
    for i in range(len(comparsions_res)):
        file.write('\n')
        for j in range(len(comparsions_res[i])):
            space = max_len - len(comparsions_res[i][j])
            file.write('%s: ' % (comparsions_res[i][j]))
            file.write(space * ' ')
            file.write('p: %s' % str(p_res[i][j]))
            file.write('\t Z: %s' % str(z_res[i][j]))
            file.write('\n')
    file.write('\n')
    file.close()
