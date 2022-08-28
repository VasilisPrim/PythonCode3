'''
Created on Dec 28, 2021

@author: vprimiky
'''


import math
class mytuple(tuple):
    '''
    This is the documentation of class mytuple
    '''
    mytup= ()
    def __init__(self,mytup):
        super()
        self.mytup  = mytup #Θα μπορούσαμε να γράψουμε self = tuple(mytup).Oπότε το στιγμιότυπο της ταξης μας είναι ένα tuple και απλώς αλλάζουμε τις συναρήτσεις __add__ κτλ. 
#Το κομμάτι κώδικα απο τη γραμμή 19 έως 28 το χρησιμοποιώ σε όλες τις συναρτήσεις(add,sub,mult,distance).Αλλάζει τις διαστάσεις των tuples προσθέτοντας μηδενικά όπου χρειάζεται.        
    def add(self,other):
        if len(self.mytup)>len(other):                    
            newlist = list(other)
            for i in range(len(self.mytup)-len(other)):
                newlist.append(0)
            other = tuple(newlist)
        elif len(self.mytup)<len(other):
            newlist = list(self.mytup)
            for i in range(len(other)-len(self.mytup)):
                newlist.append(0)
            self.mytup = tuple(newlist)
        somelist = []
        for i in range(len(self.mytup)):
            somelist.append(self.mytup[i] + other[i]) 
        self.mytup = tuple(somelist) 
        return self.mytup 
             
    
    def sub(self,other):
        if len(self.mytup)>len(other):
            newlist = list(other)
            for i in range(len(self.mytup)-len(other)):
                newlist.append(0)
            other = tuple(newlist)
        elif len(self.mytup)<len(other):
            newlist = list(self.mytup)
            for i in range(len(other)-len(self.mytup)):
                newlist.append(0)
            self.mytup = tuple(newlist)
        somelist = []
        for i in range(len(self.mytup)):
            somelist.append(self.mytup[i] - other[i]) 
        self.mytup = tuple(somelist) 
        return self.mytup 
    
    def mult(self,other):
        if len(self.mytup)>len(other):
            newlist = list(other)
            for i in range(len(self.mytup)-len(other)):
                newlist.append(0)
            other = tuple(newlist)
        elif len(self.mytup)<len(other):
            newlist = list(self.mytup)
            for i in range(len(other)-len(self.mytup)):
                newlist.append(0)
            self.mytup = tuple(newlist)
        sum = 0
        for i in range(len(self.mytup)):
            sum +=self.mytup[i]*other[i]
         
        return sum
           
    def distance(self,other):
        if len(self.mytup)>len(other):
            newlist = list(other)
            for i in range(len(self.mytup)-len(other)):
                newlist.append(0)
            other = tuple(newlist)
        elif len(self.mytup)<len(other):
            newlist = list(self.mytup)
            for i in range(len(other)-len(self.mytup)):
                newlist.append(0)
            self.mytup = tuple(newlist)
        sum = 0
        for i in range(len(self.mytup)):
            sum +=(self.mytup[i] - other[i])**2
        return round(math.sqrt(sum),3)
    
    def __add__(self,other):
        return self.add(other)
    def __mul__(self,other):
        return self.mult(other)
    def __sub__(self,other):
        return self.sub(other)





