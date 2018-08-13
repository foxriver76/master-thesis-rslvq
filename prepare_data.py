#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:11:46 2018

@author: moritz
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

"""This file prepares the real world data streams by reading the csv,
doing One hot encoding, standardization, removing the id column,
replace missing values and writing it to a new csv-file"""

#airlines_df = pd.read_csv('datasets/airlines.csv') # do all
cover_df = pd.read_csv('datasets/covtypeNorm.csv') # remove id first column
electricity_df = pd.read_csv('datasets/elecNormNew.csv') # remove id, ohe for label
#kdd_df = pd.read_csv('datasets/kddcup.data_10_percent_corrected.csv') # do all
poker_df = pd.read_csv('datasets/poker-lsn.csv') # normalize
gmsc_df = pd.read_csv('datasets/gmsc-train.csv')

"""Drop id column"""
#airlines_df = airlines_df.drop(['id'], axis=1)
cover_df = cover_df.drop(['id'], axis=1)
electricity_df = electricity_df.drop(['id'], axis=1)
#kdd_df = kdd_df.drop(['id'], axis=1)
poker_df = poker_df.drop(['id'], axis=1)

gmsc_labels = gmsc_df['SeriousDlqin2yrs']
gmsc_df = gmsc_df.drop(['SeriousDlqin2yrs'], axis=1)
gmsc_df = gmsc_df.drop(gmsc_df.columns[0], axis=1)
gmsc_df = gmsc_df.join(gmsc_labels)
gmsc_df = gmsc_df.dropna(how='all')

"""Replace NaN"""
gmsc_df = gmsc_df.replace([np.inf, -np.inf], np.nan).dropna(axis=0)

"""OHE"""
#from sklearn.preprocessing import LabelEncoder
#from sklearn.preprocessing import OneHotEncoder
#
#ohe = pd.get_dummies(airlines_df[['Airline', 'AirportFrom', 'AirportTo']])
#airlines_df = airlines_df.drop(['Airline', 'AirportFrom', 'AirportTo'], axis=1)
#airlines_df = airlines_df.join(ohe)
## poker_df is numeric

elec_classes = ['UP', 'DOWN']
electricity_df['class'] = electricity_df['class'].apply(elec_classes.index)

"""Standardization"""
#stdsc = StandardScaler()
#X, y = gmsc_df.iloc[:, 1:].values, gmsc_df.iloc[:, 0].values
#X_std = stdsc.fit_transform(X)

"""Save as csv"""
electricity_df.to_csv('datasets/electricity_final.csv')
gmsc_df.to_csv('datasets/gmsc_final.csv')
poker_df.to_csv('datasets/poker_final.csv')
cover_df.to_csv('datasets/cover_final.csv')