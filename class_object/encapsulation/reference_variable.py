"""
reference Variable
pass by value/ pass by reference

"""

class Customer:
    """suppose 

    we are doing 
    
    Atm()

    here a object is created is store in the memory but we cannot accessed it as we donot sotre it some variable which
    refer it so we do:
    sbi = Atm()
    where sbi is the reference variable which points to the address of the object and Atm() is the object
   
    
    """


    def __init__(self,name,gender):
       self.name = name 
       self.gender = gender

def greet(customer):
    if customer.gender =="male":
        print("hello", customer.name, "sir")
    else:
        print("hello", customer.name, "smaam")

    cust2 = Customer("kamini","female")
    return cust2



cust = Customer("lamini", "male")

new_cus =greet(cust) # we are passing object of class to the function and function can return that object as well. 
print(new_cus.name)



# pass by reference



class Customer:


    def __init__(self,name):
       self.name = name 

def greet(customer):
    print(id(cust))


    print("hello", customer.name, "sir")
    



cust = Customer("lamini")
print(id(cust))
greet(cust) # as we sending refernce variable to the function greet. the reference variable  refer to object variable 
#lamini also greet is refer to object 


#pass by value


class Customer:


    def __init__(self,name):
       self.name = name 

def greet(customer):
    print(id(customer))

    customer.name ="garvit"   
    print(id(customer))
 



cust = Customer("lamini")
print(id(cust))
greet(cust)

print(cust.name)
         #  we are passing object to function greet and inside the function we changing the object variable to "garvit "
         # so outside the function value of object variable is changed
         # 
         # class object are mutables.   we see in greet function first     print(id(customer))
 #second     print(id(customer)) are same . Also     print(id(cust)) is also same. 
  
 
 ###################################################
 # collection of objects
  
 
class Customer:


    def __init__(self,name, age):
       self.name = name 
       self.age = age

    def intro(customer):
        print(f"mu name is {customer.name} and my age is {customer.age}" )

c1= Customer("kamni",23)
c2= Customer("manisha",34)

L = [c1,c2]
print(L) #address
print("*************************************************")
for i in L:
    
    i.intro()

