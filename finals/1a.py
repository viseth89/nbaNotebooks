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


cavs = [cc1, cc2, cc3, cc4, cc5, cc6, cc7]
warr = [gs1, gs2, gs3, gs4, gs5, gs6, gs7]

cassists = []
crebounds = []
for game in cavs:
    '''
    print("Teamstats")
    print(game.iloc[-1,:])
    '''
    cassists.append(int(game.iloc[-1,-7]))
    crebounds.append(int(game.iloc[-1,-8]))
    
wassists = []
wrebounds = []
for game in warr:
    '''
    print("Teamstats")
    print(game.iloc[-1,:])
    '''
    wassists.append(int(game.iloc[-1,-7]))
    wrebounds.append(int(game.iloc[-1,-8]))
    
    
    
    #Create a game class
print (cassists)
print (crebounds)
print('viseth')
print(wrebounds)
print(wassists)
#Addding of two lists
total = [sum(x) for x in zip(cassists, wassists)]
print ('total for assists')
print (total)
rebounds = [m - n for m,n in zip(crebounds,wrebounds)]
      #adding and subtracting zip method of two lists      
reboundz = [m + n for m,n in zip(crebounds,wrebounds)]
print ('rebounds')
print (rebounds)
print ('reboundz')
print (reboundz)

 

#returning objects to list

#Last of Cleveland
'''
cassists = cc1a + cc2a + cc3a + cc4a + cc5a + cc6a + cc7a
print (cassists/7)

# find the count of cassists so we can divide by 7 using programming

print ("cleveland assists vavasdf")


cleveland = [cc1a, cc2a, cc3a, cc4a, cc5a, cc6a, cc7a, cassists]
print(cleveland)
print(cleveland[-1])
'''


'''

print ("assists " + str(assists))


'''