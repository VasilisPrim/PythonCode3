'''
Created on Dec 28, 2021

@author: vprimiky
'''
myList = [[[(x,y,z) for x in range(1,7)] for y in range(1,7)] for z in range(1,7) ]

myDict = {}
for i in myList:
    for j in i:
        for k in j:
            sum = k[0] + k[1] + k[2]
            if  tuple(sorted(k)) in myDict:
                y = myDict[tuple(sorted(k))]
                y[0]  = y[0] + 1
                myDict[tuple(sorted(k))] = [y[0],sum]
            else:
                myDict[tuple(sorted(k))] = [1,sum]
            
sortedDict1 = sorted(myDict.items(),key = lambda item:item[1][0],reverse=True ) 
sortedDict2 = sorted(myDict.items(),key = lambda item:item[1][1],reverse=True )            
            
            
for i in range(0,len(sortedDict1)):
    print(sortedDict1[i][1])            
print("---------------------------------")
for i in range(0,len(sortedDict2)):
    print(sortedDict2[i][1])
