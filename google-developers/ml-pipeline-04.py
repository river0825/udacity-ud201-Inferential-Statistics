#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 19:33:12 2017

@author: river
"""
from sklearn import datasets
iris = datasets.load_iris()

X = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .8)

#from sklearn import tree
#clf = tree.DecisionTreeClassifier()

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()



clf.fit(X_train, y_train)
predict = clf.predict(X_test)

from sklearn.metrics import accuracy_score

print (accuracy_score(y_test, predict))
