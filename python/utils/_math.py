'''
Author: zwx
LastEditTime: 2023-07-10 20:06:46
Description: 
'''
import math
import numpy as np

'''
description: N
param {*} x
param {*} mu
param {*} sigma
return {*}
'''
def normal(x, mu, sigma):
    p = 1 / math.sqrt(2 * math.pi * sigma**2)
    return p * np.exp(-0.5 / sigma**2 * (x - mu)**2)