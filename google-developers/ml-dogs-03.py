#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 19:23:05 2017

@author: river
"""

import numpy as np
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500

grey_height = 28 + 4 * np.random.randn(greyhounds)
lab_height = 28 + 4 * np.random.randn(labs)

plt.hist([grey_height, lab_height], stacked= True, color=['r', 'b'])
plt.show()

#height is not enoug to identity what breed of dog is
#add features

# useless data as eys color

#independ features are good

# avoid redundant features
# feature easy to understand
