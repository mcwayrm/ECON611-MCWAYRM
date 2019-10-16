#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 14:39:21 2019

@author: stephenembry

This scrapes the data for the child welfare program in nber and dumps it
into a json file
"""

import json
import requests
from bs4 import BeautifulSoup

def extract_and_prettify_text(site):
    r = requests.get(site)
    return r.text
    #soup = BeautifulSoup(r.text)
    #return soup.text#.prettify()


main_site = requests.get('https://www.nber.org/papersbyprog/CH.html')
main_soup = BeautifulSoup(main_site.text)
paper_sites = [a['href'] for a in main_soup.find_all(href=True) if \
               'https://www.nber.org/papers/w' in a['href']]
paper_texts = [extract_and_prettify_text(site) for site in paper_sites]
with open('texts.json', 'w') as f:
    json.dump(paper_texts, f)