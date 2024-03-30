# abstraction : hidden to apply constrait
'''
you are senior most developer n u are going to develop a bankapp  which is inherited by 
webapp and mobile app.you want if webapp and mobileapp inherit the bank app they have to
implement a security method in their class bank app have thwo method databse connection
and secruity where secuirty is the abtract method

abstract method is the method which is have no code but for child class, implementaion 
is different for secuirty.we make abstract class by sing abc(abstract class)  ABC and 
abstract method. that class should have atleat one abstract method. also we cannot make
object of abstract class when web app and mobile app will inherit from the bank app and 
'''


from abc import ABC, abstractmethod

class BankApp(ABC):

    def database(self):
        print("connected to databse")
    
    @abstractmethod
    def security(self):
        pass


class WebApp(BankApp):

    def login(self):
        print("login to website")

# c = WebApp()

# c.login()

# this will give error TypeError: Can't instantiate abstract class WebApp with abstract methods security

# thereofre we have to include a security meyhod in webapp




from abc import ABC, abstractmethod

class BankApp(ABC):

    def database(self):
        print("connected to databse")
    
    @abstractmethod
    def security(self):
        pass


class WebApp(BankApp):

    def login(self):
        print("login to website")

    def security(self):
        print("secuirtu for webapp")

c = WebApp()

c.login()
c.database()
c.security() #method overriding

