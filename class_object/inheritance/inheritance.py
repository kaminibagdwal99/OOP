
"""
code reuselibility

a child class can inherit attribute and methods of parent class

                      User(parent )
                       ||
                    --login
                    --register
        -------------------------------------------
        Student(child)                         instructor (child)            
           ||                                      ||
        --enroll                                --create course
        --review                                --reply

"""

class User:

    def __init__(self):
        self.name = "kamini"

    def login():
        print("l")

    def register():
        pass

class Student(User): #it tell python that user is parent clss and Student is child
    # class and child class can access child class as well as student class. 
    #
    

    def enroll():
        print("enroll")


c = Student()
u = User()

print(c.name)

############# What things are inherited from parent class################################
    #  constructor , non private attibute, non private method
    #method overloading if child has constructor it will not access the parent construtor from parent class.
                                                                                                                                                                        


########class disgram if it has triangle it is inheritance parent head will be towars parent class.


# 1 concept: constructor example

class Phone:
    def __init__(self, price, model) :
        print("inside phone constructor")
        self.price = price
        self.model= model

    def buy(self):
        print("buy")



class Nokia(Phone):
    pass

c = Nokia(122,"samsung")
print(c.model)
c.buy()

### 2 concept : constructor with both have constructor
class Phone:
    def __init__(self, price, model) :
        print("inside phone constructor")
        self.price = price
        self.model= model

    def buy(self):
        print("buy")



class Nokia(Phone):
    def __init__(self, os, ram):
        print("inside noKia constructor")
        self.ram = ram
        self.os = os

c = Nokia("samsung",22) # it will initilaze child constructor . if child has its own constructor so parent constructor 
#will be not insiliaze and cannot access parent varible, 



### 3. concept : child object cannot access private attibutes and methods of parent class

class Phone:
    def __init__(self, price, model) :
        print("inside phone constructor")
        self.__price = price
        self.model= model

    def show(self):
        print(self.__price) #AttributeError: 'Nokia' object has no attribute '_Nokia__price'



class Nokia(Phone):
    def check(self):
        print(self.model)
        print(self.__price)

c = Nokia(122,"oneplus")
# c.check()


#example 1

class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num #getter method

class Child(Parent):
    def show(self):
        print("this is child")


son = Child(100)
print(son.get_num())
son.show()


#example 2


class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num #getter method  AttributeError: 'Child' object has no attribute '_Parent__num'
        # as init of parent wil be called

class Child(Parent):


    def __init__(self, val,num):
        self.__val = val

  
    def get_val(self):
        return self.__val #getter method


son = Child(100, 10)
print("child val", son.get_val())
# print("parent num" ,son.get_num())


#example 3

class A:
    def __init__(self) -> None:
        self.var1 = 100

    def display1(self,var1):
        print("class a", self.var1, var1)# var1 and self.var1 are different

class B(A):
    def display2(self, var1):
        print("class b", var1)

obj = B()
obj.display1(200)

# Method overriding
 #if child class and parent class both have method with same name then class method will be called.
class Phone:
    def __init__(self, price, model) :
        print("inside phone constructor")
        self.__price = price
        self.model= model

    def buy(self):
        print("phone") 



class Nokia(Phone):
    def buy(self):
        print("smartphone")

c = Nokia(122,"oneplus")
c.buy()


# so if we have both constructor and we want to access parent variable we can do by using super() or
 #if child class and parent class both have method with same name then class method will be called. but we want to access 
 #parent we can do it by super()


class Phone:
    def __init__(self, price, model) :
        print("inside phone constructor")
        self.__price = price
        self.model= model

    def buy(self):
        print("phone") 



class Nokia(Phone):
    def buy(self):
        print("smartphone")
        super().buy()

c = Nokia(122,"oneplus")
c.buy()


#2

class Phone:
    def __init__(self, price, model) :
        print("inside phone constructor")
        self.price = price
        self.model= model

    def buy(self):
        print("buy")



class Nokia(Phone):
    def __init__(self, os, ram, price,model):
        print("inside noKia constructor")
        super().__init__(price,model)
        self.ram = ram
        self.os = os
        print("inside noKia constructor")


s = Nokia("snapdragon",22,10000,"samsung")

print(s.os)
print(s.model)

# super keyword is used inside child class and can't access variable but can access method

##summary
"""
1. A class can inherhit another class
2. constructor, attibute , method can be inherit to another class
3. Parent class has no acccess tio chikd class
4. private properties of parent clas are not accesssible to child class.
5. child class can overdide thge method and attibute . this is call method overrinding.
6. super is a inbuilf function which is used to invoke the parent class method and constructor
"""


#pratice 


class Parent:
    def __init__(self, num):
        self.__num = num

    def get_num(self):
        return self.__num #getter method  AttributeError: 'Child' object has no attribute '_Parent__num'
        # as init of parent wil be called

class Child(Parent):


    def __init__(self, val,num):
        super().__init__(num)
        self.__val = val

  
    def get_val(self):
        return self.__val #getter method


son = Child(100, 10)
print("child val", son.get_val())
print("parent num" ,son.get_num())



#2 


class Parent:
    def __init__(self):
        self.num = 100


class Child(Parent):


    def __init__(self):
        super().__init__()
        self.val = 200
  
    def get_val(self):
        print( self.num)

        print( self.val )


son = Child()
son.get_val()

 


