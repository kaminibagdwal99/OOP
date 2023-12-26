"""
1. single 
2. multilevel
 3. hirearchical
 4. multiple (diamojnd problem)
 5. hybrid
"""

#single :


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


#multilevel
class Product:
    def review(self):
        print("product customer review")

class Phone(Product):
    def __init__(self, price, model) :
        print("inside phone constructor")
        self.__price = price
        self.model= model

    def buy(self):
        print("phone") 



class Nokia(Phone):
    
    pass

s =  Nokia(2000,"snapdragon") 

s.buy()
s.review()


#Hierarical


class Phone(Product):
    def __init__(self, price, model) :
        print("inside phone constructor")
        self.__price = price
        self.model= model

    def buy(self):
        print("phone") 



class Nokia(Phone):
    
    pass

class Samsung(Phone):
    pass


n = Nokia(1000, "snapdragon").buy()
s = Samsung(19,"dragin").buy() 

# Multiple
print("#"*20)
class Phone:
    def __init__(self,price, model):
        self.__price = price
        self.model = model

    def buy(self):
        print("buying a phone")

class Product:
    def review(self):
        print("customer review")

class SmartPhone(Product, Phone):
    pass

s = SmartPhone(1000,"lava")

s.buy()
s.review()


#the diamond problem ( MRO : method resolution order)

class Phone:
    def __init__(self,price, model):
        self.__price = price
        self.model = model

    def buy(self):
        print("buying a phone")

class Product:
    def buy(self):
        print("customer review")

class SmartPhone(Phone,Product ):
    pass

s = SmartPhone(1000,"lava")

s.buy()

print("#"*20)


# example 

class A:
    def m1(self):
        return 20

class B(A):
    def m1(self):
        return 30 

    def m2(self):
        return 40


class C(B):
    def m2(self):
        return 20

ob1 = A()
ob2 = B()
ob3 = C()
print(ob1.m1()+ ob3.m1()+ ob3.m2())

#example 2

class A:
    def m1(self):
        return 20

class B(A):
    def m1(self):
        val = super().m1()+30
        return val



class C(B):
    def m1(self):
        val = self.m1()+20
        return val


ob3 = C()
print(ob3.m1()) #infinte loop