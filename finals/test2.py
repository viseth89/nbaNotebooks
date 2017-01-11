#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:14:11 2016

@author: visethsen
"""

#using Ray's Code

import glob
from csv import DictReader

def process_file(filename):
    print("Processing " + filename)
    with open(filename) as file_object:
        csv_reader =  DictReader(file_object)
        for line in csv_reader:
            print(line)

for filename in glob.glob('*.csv'):
    process_file(filename)