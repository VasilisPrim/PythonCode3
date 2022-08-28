'''
Created on Dec 28, 2021

@author: vprimiky
'''
class Employee:
    '''
    This is the documentation of class Employee
    '''
    employee_list  = []
    def __init__(self,name,address,phone_num,email,salary):
        self.name = name
        self.address = address
        self.phone_num = phone_num
        self.email = email
        self.salary = salary
        Employee.employee_list.append(self)
    
class Manager(Employee):
    '''
    This is the documentation of class Manager
    '''
    def __init__(self,name,address,phone_num,email,salary,section,list_of_emp = []):
        super().__init__(name,address,phone_num,email,salary)
        self.section = section
        self.list_of_emp = list_of_emp

    def get_salary(self):
        sum = 0
        if self.section == 'General Manager':         
            for i in self.list_of_emp:
                sum = sum + i.salary
            return  self.salary + sum*0.05    
        else:
            for i in self.list_of_emp:
                sum = sum + i.salary
            return self.salary + sum*0.10 



class Worker(Employee):
    '''
    This is the documentation of class Worker
    '''

    overtime_value = 10  # Έστω πως η υπερωρία είναι 10ευρώ/ώρα
    
    def __init__(self,name,address,phone_num,email,salary,overtime = 0):
        super().__init__(name,address,phone_num,email,salary)
        self.overtime = overtime
    def get_salary(self):
        return self.salary + self.overtime*self.overtime_value             




class Associate(Employee):
    '''
    This is the documentation of class Associate
    '''
    def __init__(self,name,address,phone_num,email,salary,list_of_duties = []):
        super().__init__(name,address,phone_num,email,salary)
        self.list_of_duties = list_of_duties

    def get_salary(self):
        return self.salary 






emp1 = Worker('James Smith','larissa',1234,'james@mail.com',750,4)
emp2 = Worker('Michael Smith','larissa',1233,'michael@mail.com',750,8)
emp3 = Worker('Robert Smith','larissa',1232,'robert@mail.com',750,12)
emp4 = Associate('Maria Garcia','larissa',1234,'maria@mail.com',1100,[1,2,3])
emp5 = Associate('Maria Rodriguez','larissa',1233,'mery@mail.com',1100,[3,4,5])
emp6 = Associate('David Smith','larissa',1232,'david@mail.com',1100,[6,7,8])
emp7 = Manager('Maria Hernandez','larissa',1232,'mr@mail.com',1300,'Store',[emp1,emp2,emp3])
emp8 = Manager('Bill Williams','larissa',1232,'williams@mail.com',1500,'Office',[emp4,emp5,emp6])
emp9 = Manager('Jon Brown','larissa',1232,'brown@mail.com',2500,'General Manager',[emp7,emp8])




newList = sorted(Employee.employee_list,key = lambda x : x.get_salary(),reverse=True)
for i in newList:
    print(i.name,"---->",i.get_salary())   # οι υπολογισμοί του μισθού  για το μπόνους έγιναν με βάση το βασικό μισθό κάθε υπαλλήλου μη υπολογίζοντας το μπόνους ή τις υπερωρίες των προηγούμενων.

