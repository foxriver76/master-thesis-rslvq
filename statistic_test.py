#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 11:18:24 2018

@author: Moritz Heusinger <moritz.heusinger@gmail.com>
"""


#from scipy.stats.mstats import friedmanchisquare as Friedman
from lib import friedman_test as Friedman, bonferroni_dunn_test as Bon_dunn
import datetime

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

algorithm_names = ['RSLVQ SGD',
                   'RSLVQ ADA',
                   'RSLVQ RMS',
                   'Naive Bayes',
                   'Hoeffding Tree',
                   'Adaptive Hoeffding Tree'
                    ]

accuracys_per_algorithm = [[85.3, 71.5, 74.7], 
                         [85.3, 93.1, 75.1], 
                         [85.3, 85.8, 74.8],
                         [58.0, 14.8, 38.9],
                         [80.9, 93.2, 71.2],
                         [88.3, 88.1, 71.3]]

comparing_algorithm = 'RSLVQ ADA'

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
