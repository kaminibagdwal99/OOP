 ## aggregation has a relationship
    #inheritance : is a relationship


    # we have class customer and address . so customer has a addrss that is a aggregation
       
    
"""aggregation : on e class owns the other class.exaple: customer class owns address class     """


class Customer:

    def __init__(self,name,age,address):
        self.name =name
        self.age=age
        self.address =address

    # def print_addres( self):
    #     print(self.address.city)

class Address:

    def __init__(self, city,state,pin):
        self.city = city # if we make city as private variable we are uanle to access in customer class.
        self.state = state
        self.pin = pin



# address1 = Address("chattarpur" , "Delhi", 110089)
# c1 = Customer("kamini",23,address1)





####################################################private variable #######3


class Customer:

    def __init__(self,name,age,address):
        self.name =name
        self.age=age
        self.address =address

    def print_addres( self):
        print(self.address.get_city())

class Address:

    def __init__(self, city,state,pin):
        self.__city = city # if we make city as private variable we are uanle to access in customer class.
        self.state = state
        self.pin = pin
 
 # if we want to make city as private and we want to access the _city we will uset getter method
    def get_city(self):
        return self.__city


address1 = Address("chattarpur" , "Delhi", 110089)
c1 = Customer("kamini",23,address1)

######### Editing profile ###################################################################333


class Customer:

    def __init__(self,name,age,address):
        self.name =name
        self.age=age
        self.address =address

    
    def print_address( self):
        print(self.name, self.address.city, self.address.state, self.address.pin)

    def edit_profile(self,new_name,new_city,new_state, new_pincode):
        self.name = new_name
        self.address.change_address(new_city, new_state,new_pincode)

class Address:

    def __init__(self, city,state,pin):
        self.city = city
        self.state = state
        self.pin = pin

    def change_address(self,new_city, new_state,new_pincode):
        self.city = new_city
        self.state = new_state
        self.pincode = new_pincode


address1 = Address("new_delhi", "Delhi", 110089)
c1 = Customer("kamini",23,address1)

c1.print_address()

c1.edit_profile("garvit","almora","uk",110078)

c1.print_address()



#class diagramme
"""

customer has diamond relationship with address, customer has diamond

Customer
--------------------------------------
name
gender
address
--------------------------------------
printaddress
edit_address

____________________________________

Address
----------------------------------------------
-city # minus sign show private variable
address
----------------------------------------------
edit_address

"""