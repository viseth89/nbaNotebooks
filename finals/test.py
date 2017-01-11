#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:14:47 2016

@author: visethsen
"""

1
2
import pandas
data_df = pandas.read_csv('gs3.csv')

'''
#Creating a variable = The Brackets are to indicate position
[0:5,:] = The first 5 rows and all the columns
[:,0:5] = All the rows and the first 5 columns
data_df.iloc <---- ILOC is the command for location, 
data_df is the variable we created to hold the csv information 

'''

starters = data_df.iloc[0:5,:]

print(data_df)
print ('')

print(data_df.iloc[-1,-2])
print(data_df.shape)


print('starters')
print(starters)

#Code to print out the points scored by the starters 
print(starters.iloc[:,-2])