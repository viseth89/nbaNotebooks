#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 11:03:32 2016

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


#For Loop to iterate through each game in the list, appending the stats to the empty variables created.
for game in cavs:
    cast.append(game.iloc[-1,-7])
    cstl.append(game.iloc[-1,-6])
    crbs.append(game.iloc[-1,-8])
    corbs.append(game.iloc[-1,-10])
    cpts.append(game.iloc[-1,-2])
    vs.append(game.tail(1)['PTS'])
    vt.append(game.tail(1)['AST'])

    '''
    this command not working
    
    vs.append(cc1.tail(5)['PTS'])
    
    but this one does?
    
    cc1.tail(1)['PTS']
    
    vs
Out[59]: 
[13    89
 Name: PTS, dtype: int64, 13    77
 Name: PTS, dtype: int64, 13    120
 Name: PTS, dtype: int64, 13    97
 Name: PTS, dtype: object, 13    112
 Name: PTS, dtype: object, 13    115
 Name: PTS, dtype: object, 8    93
 Name: PTS, dtype: int64]

cpts
Out[60]: [89, 77, 120, '97', '112', '115', 93]

want to find a different way to slice
    
    
    '''
print (cast)
print (cstl)
print('rebounds')
print (crbs)
# Want to find a how to call using .ix[-1,'AST']


for game in wars:
    wast.append(game.iloc[-1,-7])
    wstl.append(game.iloc[-1,-6])
    wrbs.append(game.iloc[-1,-8])
    worbs.append(game.iloc[-1,-10])
    wpts.append(game.iloc[-1,-2])
    

plt.figure(1)    
plt.plot(games,cpts,'g', label = 'Points')
plt.plot(games,cast,'c', label = 'Assists')
plt.plot(games,crbs,'r', label = 'Rebounds')
plt.plot(games,corbs,'m', label = 'O Rebounds')
plt.plot(games,cstl,'b', label = 'Steals')

plt.title('Cleveland Cavaliers')
plt.xlabel('Game for C')
plt.legend()
plt.show()

plt.figure(2)
plt.plot(games,wpts,'g',label ='Pts')
plt.plot(games,wast,'c',label='Assist')
plt.plot(games,wrbs,'r', label = 'Rebounds')
plt.plot(games,worbs,'m', label = 'O Rebounds')
plt.plot(games,wstl,'b', label = 'Steals')

plt.title('Golden State Warriors')
plt.xlabel('Game')
plt.legend()
plt.show()

'''
>>> df.recency
>>> df['recency']
>>> df[['recency']]
>>> df.loc[:, 'recency']
>>> df.loc[:, ['recency']]
>>> df.iloc[:, 0]
>>> df.iloc[:, [0]]
>>> df.ix[:, 0]
'''