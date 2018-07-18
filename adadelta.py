#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 11:14:23 2018

@author: moritz
"""

import numpy as np
import matplotlib.pyplot as plt

def _costf(x, w, **kwargs): # RSLVQ cost function
    d = (x - w)[np.newaxis].T 
    d = d.T.dot(d)
    return -d / (2 * 0.5) # sigma = 0.5

def adadelta(x1, training_data, decay_rate=0.9, epsilon=1e-8, n_steps=10000):
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
    n_steps : int, optional (default=10000)
        Number of updates
    """
    x = np.asarray(x1)
    errors = np.zeros(n_steps)
    for proto in x:
        print(proto)
        # Initialize accumulation variables
        squared_mean_gradient = np.zeros_like(proto)
        squared_mean_step = np.zeros_like(proto)
        steps = np.zeros((n_steps, proto.shape[0])) 
        for i in range(n_steps): # Loop over number of updates
            # Compute gradient
            gradient = np.gradient(proto)
            
            # Accumulate gradient
            squared_mean_gradient = decay_rate * squared_mean_gradient + \
                                    (1 - decay_rate) * gradient ** 2 
            
            # Compute update/step
            steps[i] = (-((squared_mean_step + epsilon) / \
                         (squared_mean_gradient + epsilon)) ** 0.5) * gradient
            
            # Accumulate updates
            squared_mean_step = decay_rate * squared_mean_step + (1 - decay_rate) * steps[i] ** 2
            
            # TODO: Update weights according to costfunction (should do this in Adadelta)
            # TODO: Handle Batch_Size
            # Apply update
            proto += steps[i]
            
            # Calculate Error
            errors[i] = _costf(x=training_data, w=proto) # _optfun should be the correct choice to minimize
         
#    plt.plot(steps)    
#    plt.ylabel('Absolute Step')
#    plt.xlabel('Iteration number')
#    plt.show()
    
    plt.plot(errors)
    plt.ylabel('Error')
    plt.xlabel('# Iterations')
    plt.show()
    

# Execute Adadelta
x = adadelta(x1=[[  3.86442072,  -8.67346152],
                 [  4.25960116, -10.19065868],
                 [  4.15062386,  -9.02946862],
                 [  4.5047864,  -9.85700446],
                 [ -3.75065403,  -0.23810625],
                 [ -4.15312578,  -0.83056292],
                 [ -3.58535989,  -0.62365679],
                 [ -3.85306309,  -0.08282406],
                 [  0.62290859,  -5.49401842],
                 [  0.85739039,  -4.93796399],
                 [  0.21804012,  -5.63702014],
                 [  0.32490749,  -4.06178612],
                 [ -1.8286395,    6.4499625 ],
                 [ -1.35754436,   6.56678368],
                 [ -1.88426733,  8.43300056],
                 [ -1.45034838,   7.61238691]], 
             training_data=[1.5, 0.5], 
             n_steps=10000, decay_rate=0.9)

"""
    def _optgrad(self, variables, training_data, label_equals_prototype,
                 random_state):
        n_data, n_dim = training_data.shape
        nb_prototypes = self.c_w_.size
        prototypes = variables.reshape(nb_prototypes, n_dim)

        g = np.zeros(prototypes.shape)
        for i in range(n_data):
            xi = training_data[i]
            c_xi = label_equals_prototype[i]
            for j in range(prototypes.shape[0]):
                d = (xi - prototypes[j])
                c = 1 / self.sigma
                if self.c_w_[j] == c_xi:
                    g[j] += c * (self._p(j, xi, prototypes=prototypes, y=c_xi) -
                                 self._p(j, xi, prototypes=prototypes)) * d
                else:
                    g[j] -= c * self._p(j, xi, prototypes=prototypes) * d
        g /= n_data
        g *= -(1 + 0.0001 * random_state.rand(*g.shape) - 0.5)
        return g.ravel()
"""