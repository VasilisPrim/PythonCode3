'''
Created on Dec 28, 2021

@author: vprimiky
'''


def intersect(list1,list2):
    return [i for i in list1 if i in list2]
    

while True:
    try:
        list1 = input("Give the first list: ").strip("[,],' '").split(",")
        for i in range(len(list1)):
            list1[i] = int(list1[i])
         
        list2 = input("Give the second list: ").strip("[,],' '").split(",")
        for i in range(len(list2)):
            list2[i] = int(list2[i])
        break    
        
    except:
        print("You gave a string as input in the list not an integer!")
        print("Do you want to try again?(y/n)")
        answer = input("Your choice: ").lower().strip()
        if answer != "y":
            break
        continue      


intersection_list = sorted(intersect(list1,list2))
print(intersection_list)
