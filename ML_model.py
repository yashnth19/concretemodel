# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 21:33:17 2022

@author: Yreddy
"""

import pickle
from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import Ridge,Lasso ,RidgeCV,LassoCV , ElasticNet , ElasticNetCV,LinearRegression
from sklearn.model_selection import train_test_split

model=pickle.load(open('linear_reg.sav','rb'))
