#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:11:46 2018

@author: moritz
"""

import pandas as pd

"""This file prepares the real world data streams by reading the csv,
doing One hot encoding, standardization, removing the id column,
replace missing values and writing it to a new csv-file"""

airlines_df = pd.read_csv('datasets/airlines.csv') # do all
cover_df = pd.read_csv('datasets/covtypeNorm.csv') # remove id first column
electricity_df = pd.read_csv('datasets/elecNormNew.csv') # remove id, ohe for label
kdd_df = pd.read_csv('datasets/kddcup.data_10_percent_corrected.csv') # do all
poker_df = pd.read_csv('datasets/poker-lsn.csv') # normalize

"""Drop id column"""
airlines_df = airlines_df.drop(['id'], axis=1)
cover_df = cover_df.drop(['id'], axis=1)
electricity_df = electricity_df.drop(['id'], axis=1)
#kdd_df = kdd_df.drop(['id'], axis=1)
poker_df = poker_df.drop(['id'], axis=1)

"""Replace NaN"""
# Currently no dataset has NaN

"""OHE"""
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

ohe = pd.get_dummies(airlines_df[['Airline', 'AirportFrom', 'AirportTo']])
airlines_df = airlines_df.drop(['Airline', 'AirportFrom', 'AirportTo'], axis=1)
airlines_df = airlines_df.join(ohe)
# poker_df is numeric



"""Standardization"""

"""Save as csv"""