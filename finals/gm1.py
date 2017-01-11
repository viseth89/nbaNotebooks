"""

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


cc1a = int(cc1.iloc[-1,-7])

cc2a = int(cc2.iloc[-1,-7])

cc3a = int(cc3.iloc[-1,-7])

cc4a = int(cc4.iloc[-1,-7])

cc5a = int(cc5.iloc[-1,-7])

cc6a = int(cc6.iloc[-1,-7])

cc7a = int(cc7.iloc[-1,-7])

#Last of Cleveland

cassists = cc1a + cc2a + cc3a + cc4a + cc5a + cc6a + cc7a

ccassists = {"Game 1 Assist" : cc1a, 
             "Game 2 Assist" : cc2a, 
             "Game 3" : cc3a,
             "Game 4" : cc4a,
             "Game 5" : cc5a,
             "Game 6" : cc6a,
             "Game 7" : cc7a,}

print (ccassists["Game 3"] + ccassists["Game 4"])
print (ccassists)

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