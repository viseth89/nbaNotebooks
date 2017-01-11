#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 20:28:20 2016

@author: visethsen
"""
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style

# variable used to represent games
games = [1,2,3,4,5,6,7]

#Creating Varibles to hold the Read CSV Files
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
#creating temp variables

#Creating a list to hold the games with empty variables to store the stats
wars = [gs2,gs2,gs3,gs4,gs5,gs6,gs7]
wpts = []
wrbs = []
wast = []
wstl = []
worbs = []



class Game:
    def __init__(self, name, file):
        self.name = name
        self.PTS = file.iloc[-1,-2]
        self.STL = file.iloc[-1,-6]
        self.RBS = file.iloc[-1,-8]
        self.ORBS = file.iloc[-1,-10]

for x in range(0,len(cavs)):
    for game in cavs:
        game[x] = Game('name', game)