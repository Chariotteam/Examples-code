#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 16:59:43 2021

@author: timur
"""

import random
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def generate_models(x, y, degs):
    
    models = []
    for deg in degs:
        model = np.polyfit(x,y,deg)
        models.append(model.tolist())
    return models

def compare_values(y1, y2):
    y = np.array(y1)
    estimated = np.array(y2)
    mean_error = (((estimated - y)**2).sum())/len(y)
    return 1 - (mean_error/np.var(y))

def compare(y, estimated):
    mean_error = (((estimated - y)**2).sum())/len(y)
    return 1 - (mean_error/np.var(y))
 
def l_predict(model, x):

    results = np.polyval(model, x)
    return results.tolist()

def splitData(xVals, yVals, n):
    toTrain = random.sample(range(len(xVals)),
                            len(xVals)//n)
    trainX, trainY, testX, testY = [],[],[],[]
    for i in range(len(xVals)):
        if i in toTrain:
            trainX.append(xVals[i])
            trainY.append(yVals[i])
        else:
            testX.append(xVals[i])
            testY.append(yVals[i])
    return trainX, trainY, testX, testY



def cross_validating(x,y, degrees, subsets, n):
    rSquares = {}
    xVals = np.array(x)
    yVals = np.array(y)
    for f in range(subsets):
        trainX, trainY, testX, testY = splitData(xVals, yVals,n)
        for d in degrees:
            model = np.polyfit(trainX, trainY, d)
            estYVals = np.polyval(model, testX)
            if d in rSquares.keys():
                rSquares[d].append(compare(testY, estYVals))
            else:
                rSquares[d] = []
                rSquares[d].append(compare(testY, estYVals))
                
    results = {}
    best_degree = degrees[0]
    best_mean = sum(rSquares[best_degree])/len(rSquares[best_degree])
    
    for d in degrees:
        mean = sum(rSquares[d])/len(rSquares[d])
        std = np.std(rSquares[d])
        results[d] = (mean,std)
        if mean > best_mean:
            best_mean = mean
            best_degree = d
        
    return best_degree

data = pd.read_csv("data_main.csv")
all_x = data['kg'].values.tolist()
all_y = data['m'].values.tolist()
var = int(len(all_x)*0.9)
predict_x = all_x[var:]
train_x = all_x[:var]
predict_y = all_y[var:]
train_y = all_y[:var]
print("x:",predict_x, train_x)
print("y:",predict_y, train_y)
subsets = 100
n = 2
degrees = list(range(17))
best_degree = cross_validating(train_x,train_y, degrees, subsets, n)

print(best_degree)


model = np.polyfit(train_x, train_y, best_degree)

estY = np.polyval(model, predict_x)

print(compare(predict_y, estY))
