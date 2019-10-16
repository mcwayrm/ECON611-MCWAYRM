#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:22:29 2019

@author: stephenembry
"""

import json
import pandas as pd


def load_data():
    df = pd.read_csv('../database/AB_NYC_2019.csv')
    df = df[['id', 'host_id', 'neighbourhood_group', 'neighbourhood', 'price', 
         'minimum_nights', 'room_type']]
    df.set_index('id', inplace=True)
    return json.loads(df.to_json(orient='index'))