#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:06:34 2016

TODO :
    
1. Create a Dictionary for each game HOlding the TOtals of all games
2. Main Stats in the Team total will be Assists, rebounds, offensive rb, stl, 




@author: visethsen
"""

import pandas

cc1 = pandas.read_csv('cc1.csv')
gs1 = pandas.read_csv('gs1.csv')
cc2 = pandas.read_csv('cc2.csv')
gs2 = pandas.read_csv('gs2.csv')
cc3 = pandas.read_csv('cc3.csv')
gs3 = pandas.read_csv('gs3.csv')
cc4 = pandas.read_csv('cc4.csv')
gs4 = pandas.read_csv('gs4.csv')
cc5 = pandas.read_csv('cc5.csv')
gs5 = pandas.read_csv('gs5.csv')
cc6 = pandas.read_csv('cc6.csv')
gs6 = pandas.read_csv('gs6.csv')
cc7 = pandas.read_csv('cc7.csv')
gs7 = pandas.read_csv('gs7.csv')


games = [cc1, gs1, cc2, gs2, cc3, gs3]
assists = []
for game in games:
    print("Teamstats")
    print(game.iloc[-1,:])
    assists.append(int(game.iloc[-1,-7]))
    
    #Create a game class
print (assists)
print('viseth')
#returning objects to list
'''
print("Cleveland Teamstats")
print(cc1.iloc[-1,:])
print("Cleveland Assists")
cc1a = int(cc1.iloc[-1,-7])

print("Cleveland Teamstats")
print(cc2.iloc[-1,:])
print("Cleveland Assists")
cc2a = int(cc2.iloc[-1,-7])

print("Cleveland Teamstats")
print(cc3.iloc[-1,:])
print("Cleveland Assists")
cc3a = int(cc3.iloc[-1,-7])

print("Cleveland Teamstats")
print(cc4.iloc[-1,:])
print("Cleveland Assists")
cc4a = int(cc4.iloc[-1,-7])

print("Cleveland Teamstats")
print(cc5.iloc[-1,:])
print("Cleveland Assists")
cc5a = int(cc5.iloc[-1,-7])

print("Cleveland Teamstats")
print(cc6.iloc[-1,:])
print("Cleveland Assists")
cc6a = int(cc6.iloc[-1,-7])

print("Cleveland Teamstats")
print(cc7.iloc[-1,:])
print("Cleveland Assists")
cc7a = int(cc7.iloc[-1,-7])
'''
#Last of Cleveland

cassists = cc1a + cc2a + cc3a + cc4a + cc5a + cc6a + cc7a
print (cassists/7)

# find the count of cassists so we can divide by 7 using programming

print ("cleveland assists vavasdf")


cleveland = [cc1a, cc2a, cc3a, cc4a, cc5a, cc6a, cc7a, cassists]
print(cleveland)
print(cleveland[-1])



'''
#Gs

print(gs1)
print("Golden State Teamstats")
print(gs1.iloc[-1,:])
print ('Golden State Assist')
print (gs1.iloc[-1,-7])

print("Golden State Teamstats")
print(gs2.iloc[-1,:])
print ('Golden State Assist')
print (gs2.iloc[-1,-7])

print("Golden State Teamstats")
print(gs3.iloc[-1,:])
print ('Golden State Assist')
print (gs3.iloc[-1,-7])

assists = int(gs3.iloc[-1,-7]) + int(gs2.iloc[-1,-7]) + int(gs1.iloc[-1,-7])

print ("assists " + str(assists))


'''