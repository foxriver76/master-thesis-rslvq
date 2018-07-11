#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 11:14:23 2018

@author: moritz
"""

import numpy as np

def adadelta(x1, decay_rate=0.9, e=1e-8):
    """Adadelta Gradient Optimization Algorithm based on [Zeiler, 2012]
    Parameters
    ----------
    x1 : array-like
        Weight-matrix which will be optimized
    decay_rate : int, optional (default=0.9)
        Represents the Decay Rate which determines 
        the step length of each iteration.
    e : int, optional (default=1e-8)
        A constant factor which prevents dviding by zero
    """
    # Initialize accumulation variables
    e_g = np.asarray(0)
    e_x = np.asarray(0)
    
    print('{}{}'.format(e_g, e_x))
    

adadelta(x1=[])


    
    
