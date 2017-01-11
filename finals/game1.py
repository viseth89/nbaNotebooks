#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 23:43:40 2016

@author: visethsen
"""
# Importing Matplotlib for charting, and csv to read the csv files.
from matplotlib import pyplot as plt
from matplotlib import style
import csv

#our simple way to read the csv file
with open ('f16/cc1.csv') as csvfile:
    #command to read it with arguements
    readCSV = csv.read(csvfile, delimiter=',')
    
    cpts = []
    corb=[]
    ctrb=[]
    cast=[]
    cstl=[]
    cblk=[]
    cto=[]

    points = row[]