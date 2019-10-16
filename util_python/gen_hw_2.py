#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:58:39 2019

@author: stephenembry
"""

import json
import numpy as np

#%%
def load_data():
    random_state = np.random.RandomState(1)
    items = list(range(100))
    prices = random_state.lognormal(mean=3, size=100)
    stocks = random_state.randint(low=0, high=25, size=100)
    stocks = [int(stock) for stock in stocks]
    values = [float(np.clip(random_state.normal(loc=price,
                       scale=price/2), 0, a_max=None)) for price in prices]
    print(list(zip(items, stocks, prices, values)))
    return list(zip(items, stocks, prices, values))

with open('database/hw_2.json', 'w') as f:
    json.dump(load_data(), f)
