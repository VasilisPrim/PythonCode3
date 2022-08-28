'''
Created on Dec 28, 2021

@author: vprimiky
'''


#To αρχείο περιέχει στοιχεία για τις γεννήσεις σε όλες τις πολιτείες των ΗΠΑ για το 2020 σε όλη τη διάρκεια του
#έτους.Οι στήλες που προστέθηκαν είναι το άθροισμα και ο μέσος όρος των γεννήσεων για κάθε πολιτεία σε όλη τη διάκεια του έτους.
x = open("hea.txt","w")
s = input("Filename: ")
f = open(s)
csvfile = open("mydata.csv")
newfile = open("hello.txt","w")
newstr = ""
for i in f:
    y = i.strip()
    line = y.split(',')
    mysum = sum([float(x) for x in line])
    avg = mysum/len(line)
    newstr = y+","+str(mysum)+","+str(avg)
    
    


    
print(newstr)
newfile.write(newstr)
f.close
csvfile.close
newfile.close

















