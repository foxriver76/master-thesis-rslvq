#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 09:35:11 2018

@author: moritz
"""

from __future__ import division

import math
import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.utils.multiclass import unique_labels
from skmultiflow.core.base import StreamModel
from scipy.optimize import minimize
from sklearn.utils import validation
from sklearn.utils.validation import check_is_fitted

# TODO: add sigma for every prototype (TODO from https://github.com/MrNuggelz/sklearn-lvq)

class RSLVQ(ClassifierMixin, StreamModel, BaseEstimator):
    """Robust Soft Learning Vector Quantization
    Parameters
    ----------
    prototypes_per_class : int or list of int, optional (default=1)
        Number of prototypes per class. Use list to specify different
        numbers per class.
    initial_prototypes : array-like, shape =  [n_prototypes, n_features + 1],
     optional
        Prototypes to start with. If not given initialization near the class
        means. Class label must be placed as last entry of each prototype.
    sigma : float, optional (default=0.5)
        Variance for the distribution.
    max_iter : int, optional (default=2500)
        The maximum number of iterations.
    gtol : float, optional (default=1e-5)
        Gradient norm must be less than gtol before successful termination
        of bfgs.
    display : boolean, optional (default=False)
        Print information about the bfgs steps.
    random_state : int, RandomState instance or None, optional
        If int, random_state is the seed used by the random number generator;
        If RandomState instance, random_state is the random number generator;
        If None, the random number generator is the RandomState instance used
        by `np.random`.
    gradient_descent : string, Gradient Descent describes the used technique
        to perform the gradient descent. Possible values: 'SGD' (default),
        'RMSprop', 'Adadelta'. Currently only SGD is implemented.
    Attributes
    ----------
    w_ : array-like, shape = [n_prototypes, n_features]
        Prototype vector, where n_prototypes in the number of prototypes and
        n_features is the number of features
    c_w_ : array-like, shape = [n_prototypes]
        Prototype classes
    classes_ : array-like, shape = [n_classes]
        Array containing labels.
    initial_fit: boolean, indicator for initial fitting. Set to false after
        first call of fit/partial fit.
    """

    def __init__(self, prototypes_per_class=1, initial_prototypes=None,
                 sigma=0.5, max_iter=2500, gtol=1e-5,
                 display=False, random_state=None, gradient_descent='SGD'):

        self.sigma = sigma
        self.random_state = random_state
        self.initial_prototypes = initial_prototypes
        self.prototypes_per_class = prototypes_per_class
        self.display = display
        self.max_iter = max_iter
        self.gtol = gtol
        self.initial_fit = True
        self.gradient_descent = gradient_descent

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

    def _optfun(self, variables, training_data, label_equals_prototype):
        n_data, n_dim = training_data.shape
        nb_prototypes = self.c_w_.size
        prototypes = variables.reshape(nb_prototypes, n_dim)

        out = 0

        for i in range(n_data):
            xi = training_data[i]
            y = label_equals_prototype[i]
            fs = [self._costf(xi, w) for w in prototypes]
            fs_max = max(fs)
            s1 = sum([np.math.exp(fs[i] - fs_max) for i in range(len(fs))
                      if self.c_w_[i] == y])
            s2 = sum([np.math.exp(f - fs_max) for f in fs])
            s1 += 0.0000001
            s2 += 0.0000001
            out += math.log(s1 / s2)
        return -out

    def _optimize(self, x, y, random_state):
        label_equals_prototype = y
        res = minimize(
            fun=lambda vs: self._optfun(
                variables=vs, training_data=x,
                label_equals_prototype=label_equals_prototype),
            jac=lambda vs: self._optgrad(
                variables=vs, training_data=x,
                label_equals_prototype=label_equals_prototype,
                random_state=random_state),
            method='l-bfgs-b', x0=self.w_,
            options={'disp': False, 'gtol': self.gtol,
                     'maxiter': self.max_iter})
        self.w_ = res.x.reshape(self.w_.shape)
        self.n_iter_ = res.nit
     
    def _costf(self, x, w, **kwargs):
        d = (x - w)[np.newaxis].T
        d = d.T.dot(d)
        return -d / (2 * self.sigma)

    def _p(self, j, e, y=None, prototypes=None, **kwargs):
        if prototypes is None:
            prototypes = self.w_
        if y is None:
            fs = [self._costf(e, w, **kwargs) for w in prototypes]
        else:
            fs = [self._costf(e, prototypes[i], **kwargs) for i in
                  range(prototypes.shape[0]) if
                  self.c_w_[i] == y]
        fs_max = max(fs)
        s = sum([np.math.exp(f - fs_max) for f in fs])
        o = np.math.exp(
            self._costf(e, prototypes[j], **kwargs) - fs_max) / s
        return o

    def predict(self, x):
        # copy from knn
        """Predict class membership index for each input sample.
        This function does classification on an array of
        test vectors X.
        Parameters
        ----------
        x : array-like, shape = [n_samples, n_features]
        Returns
        -------
        C : array, shape = (n_samples,)
            Returns predicted values.
        """
        check_is_fitted(self, ['w_', 'c_w_'])
        x = validation.check_array(x)
#        print('Weight Matrix for Pred: ', self.w_)
#        print('prototype classes: ' , self.c_w_)
#        print('classes: ', self.classes_)
        if x.shape[1] != self.w_.shape[1]:
            raise ValueError("X has wrong number of features\n"
                             "found=%d\n"
                             "expected=%d" % (self.w_.shape[1], x.shape[1]))

        def foo(e):
            fun = np.vectorize(lambda w: self._costf(e, w),
                               signature='(n)->()')
            pred = fun(self.w_).argmax()
            return self.c_w_[pred]

        return np.vectorize(foo, signature='(n)->()')(x)

    def posterior(self, y, x):
        """
        calculate the posterior for x:
         p(y|x)
        Parameters
        ----------
        
        y: class
            label
        x: array-like, shape = [n_features]
            sample
        Returns
        -------
        posterior
        :return: posterior
        """
        check_is_fitted(self, ['w_', 'c_w_'])
        x = validation.column_or_1d(x)
        if y not in self.classes_:
            raise ValueError('y must be one of the labels\n'
                             'y=%s\n'
                             'labels=%s' % (y, self.classes_))
        s1 = sum([self._costf(x, self.w_[i]) for i in
                  range(self.w_.shape[0]) if
                  self.c_w_[i] == y])
        s2 = sum([self._costf(x, w) for w in self.w_])
        return s1 / s2
    
    def get_info(self):
        return 'RSLVQ'
    
    def predict_proba(self, X):
        """ predict_proba
        
        Predicts the probability of each sample belonging to each one of the 
        known target_values.
        
        Parameters
        ----------
        X: Numpy.ndarray of shape (n_samples, n_features)
            A matrix of the samples we want to predict.
        
        Returns
        -------
        numpy.ndarray
            An array of shape (n_samples, n_features), in which each outer entry is 
            associated with the X entry of the same index. And where the list in 
            index [i] contains len(self.target_values) elements, each of which represents
            the probability that the i-th sample of X belongs to a certain label.
        
        """
        return 'Not implemented'
    
    def reset(self):
        self.__init__()
        
    def _validate_train_parms(self, train_set, train_lab, classes=None):
        random_state = validation.check_random_state(self.random_state)
        if not isinstance(self.display, bool):
            raise ValueError("display must be a boolean")
        if not isinstance(self.max_iter, int) or self.max_iter < 1:
            raise ValueError("max_iter must be an positive integer")
        if not isinstance(self.gtol, float) or self.gtol <= 0:
            raise ValueError("gtol must be a positive float")
        train_set, train_lab = validation.check_X_y(train_set, train_lab)

        if(classes):
            self.classes_ = np.asarray(classes)
            print('classes det: ', self.classes_)
        else:
            self.classes_ = unique_labels(train_lab)
            
        nb_classes = len(self.classes_)
        nb_samples, nb_features = train_set.shape  # nb_samples unused

        # set prototypes per class
        if isinstance(self.prototypes_per_class, int):
            if self.prototypes_per_class < 0 or not isinstance(
                    self.prototypes_per_class, int):
                raise ValueError("prototypes_per_class must be a positive int")
            # nb_ppc = number of protos per class
            nb_ppc = np.ones([nb_classes],
                             dtype='int') * self.prototypes_per_class
        else:
            nb_ppc = validation.column_or_1d(
                validation.check_array(self.prototypes_per_class,
                                       ensure_2d=False, dtype='int'))
            if nb_ppc.min() <= 0:
                raise ValueError(
                    "values in prototypes_per_class must be positive")
            if nb_ppc.size != nb_classes:
                raise ValueError(
                    "length of prototypes per class"
                    " does not fit the number of classes"
                    "classes=%d"
                    "length=%d" % (nb_classes, nb_ppc.size))
        # initialize prototypes
        if self.initial_prototypes is None:
            self.w_ = np.empty([np.sum(nb_ppc), nb_features], dtype=np.double)
            self.c_w_ = np.empty([nb_ppc.sum()], dtype=self.classes_.dtype)
            # TODO: when batch size/pretrain size is 1, the other protos will be initialized badly
            pos = 0
            print('classes: ', unique_labels(train_lab))
            print('train_lab: ', train_lab)
            for actClass in range(len(self.classes_)): #man müsste über unique train labels gehen
                nb_prot = nb_ppc[actClass] # nb_ppc:  # prototypes per class
                print('actClass={}, all_classes={}'.format(actClass, unique_labels(train_lab)))
                          #man geht aktuell davon aus, dass es für jede act class etwas gibt
                mean = np.mean(             #auf dessen basis der mean berechnet wird
                    train_set[train_lab == self.classes_[actClass], :], 0)
                self.w_[pos:pos + nb_prot] = mean + (
                        random_state.rand(nb_prot, nb_features) * 2 - 1)
                self.c_w_[pos:pos + nb_prot] = self.classes_[actClass]
                pos += nb_prot
        else:
            x = validation.check_array(self.initial_prototypes)
            self.w_ = x[:, :-1]
            self.c_w_ = x[:, -1]
            if self.w_.shape != (np.sum(nb_ppc), nb_features):
                raise ValueError("the initial prototypes have wrong shape\n"
                                 "found=(%d,%d)\n"
                                 "expected=(%d,%d)" % (
                                     self.w_.shape[0], self.w_.shape[1],
                                     nb_ppc.sum(), nb_features))
            if set(self.c_w_) != set(self.classes_):
                raise ValueError(
                    "prototype labels and test data classes do not match\n"
                    "classes={}\n"
                    "prototype labels={}\n".format(self.classes_, self.c_w_))
        print('W-matrix initialized: ', self.w_)
        self.initial_fit = False
        return train_set, train_lab, random_state

    def fit(self, X, y):
            """Fit the LVQ model to the given training data and parameters using
            l-bfgs-b.
            Parameters
            ----------
            x : array-like, shape = [n_samples, n_features]
              Training vector, where n_samples in the number of samples and
              n_features is the number of features.
            y : array, shape = [n_samples]
              Target values (integers in classification, real numbers in
              regression)
            Returns
            --------
            self
            """
            X, y, random_state = self._validate_train_parms(X, y)
            if len(np.unique(y)) == 1:
                raise ValueError("fitting " + type(
                    self).__name__ + " with only one class is not possible")
            self._optimize(X, y, random_state)
            return self
    
    def partial_fit(self, X, y, classes=None): # added
        """Fit the LVQ model to the given training data and parameters using
        l-bfgs-b.
        Parameters
        ----------
        x : array-like, shape = [n_samples, n_features]
          Training vector, where n_samples in the number of samples and
          n_features is the number of features.
        y : array, shape = [n_samples]
          Target values (integers in classification, real numbers in
          regression)
        Returns
        --------
        self
        """
        if self.initial_fit == True:
            X, y, random_state = self._validate_train_parms(X, y, classes=classes)
        elif unique_labels(y) not in self.classes_:
            raise ValueError('Class {} was not learned - please learn all \
                             classes in first call of fit/partial_fit'.format(y))
        else:
            random_state = validation.check_random_state(self.random_state)
            
        self._optimize(X, y, random_state)
        print('Weight-matrix debug: \n', self.w_)
        return self
    
    def project(self, x, dims, print_variance_covered=False):
        """Projects the data input data X using the relevance matrix of trained
        model to dimension dim
        Parameters
        ----------
        x : array-like, shape = [n,n_features]
          input data for project
        dims : int
          dimension to project to
        print_variance_covered : boolean
          flag to print the covered variance of the projection
        Returns
        --------
        C : array, shape = [n,n_features]
            Returns predicted values.
        """
        if print_variance_covered:
            print('not implemented!')
        return x[:, :dims]
    