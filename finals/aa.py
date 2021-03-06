#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:09:49 2016

@author: visethsen
"""
import pandas as pd
import matplotlib.pyplot as plt

cc1 = pd.read_csv('cc1.csv')
gs1 = pd.read_csv('gs1.csv')
cc2 = pd.read_csv('cc2.csv')
gs2 = pd.read_csv('gs2.csv')
cc3 = pd.read_csv('cc3.csv')
gs3 = pd.read_csv('gs3.csv')
cc4 = pd.read_csv('cc4.csv')
gs4 = pd.read_csv('gs4.csv')
cc5 = pd.read_csv('cc5.csv')
gs5 = pd.read_csv('gs5.csv')
cc6 = pd.read_csv('cc6.csv')
gs6 = pd.read_csv('gs6.csv')
cc7 = pd.read_csv('cc7.csv')
gs7 = pd.read_csv('gs7.csv')

#Creating a list to hold the games with empty variables to store the stats
cavs = [cc1,cc2,cc3,cc4,cc5,cc6,cc7]
cpts = []
crbs = []
cast = []
cstl = []
corbs = []

vs = []
vt = []
count=[]

#Creating a list to hold the games with empty variables to store the stats
wars = [gs2,gs2,gs3,gs4,gs5,gs6,gs7]

warriors = {
    'points' : [],
    'rebounds' : [],
    'assists' : [],
    'steals': [],
    'orebounds': []
          
          
          }
          
wpts = []
wrbs = []
wast = []
wstl = []
worbs = []

for game in cavs:
    cast.append(game.iloc[-1,-7])
    cstl.append(game.iloc[-1,-6])
    crbs.append(game.iloc[-1,-8])
    corbs.append(game.iloc[-1,-10])
    cpts.append(game.iloc[-1,-2])
    vs.append(game.tail(1)['PTS'])
    vt.append(game.tail(1)['AST'])
    
for game in wars:
    warriors['points'].append(int(game.iloc[-1,-8]))
    warriors['rebounds'].append(int(game.iloc[-1,-2]))
    warriors['assists'].append(int(game.iloc[-1,-7]))
    warriors['orebounds'].append(int(game.iloc[-1,-10]))
    warriors['steals'].append(int(game.iloc[-1,-6]))
    wast.append(game.iloc[-1,-7])
    wstl.append(int(game.iloc[-1,-6]))
    wrbs.append(game.iloc[-1,-8])
    worbs.append(game.iloc[-1,-10])
    wpts.append(game.iloc[-1,-2])
    