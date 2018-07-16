#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 11:33:19 2018

@author: moritz
"""

from climin import Adadelta
import numpy as np

def d_loss_wrt_pars(parameters, inpt, targets, predicted_labels):
    p = predicted_labels
    g_w = np.dot(inpt.T, p - targets) / inpt.shape[0]
    g_b = (p - targets).mean(axis=0)
    return np.concatenate([g_w.flatten(), g_b])

wrt = np.empty(7850)

opt = Adadelta(wrt, d_loss_wrt_pars=d_loss_wrt_pars)