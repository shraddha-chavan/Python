class Person:#base class
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
       

    def display(self):
        print("name=",self.name,"age=",self.age,"gender=",self.gender)
        

class Student(Person):#class Student inherits class Person
    pass

s1=Student('shyam',16,'m')
s=Student('ram',12,'m')#object of Student class
s.display()