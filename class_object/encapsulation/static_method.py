#static varibale


"""
static/class variable : a varibale whose value is same for each object like ifsc code they are defined
 outside the init function

"""

class Atm:
    """
   
    
    """
    counter =1 #static variable


    def __init__(self):
       self.__balance = 0  #instance variable
       self.__pin =""
       self.sno = Atm.counter
       Atm.counter +=1

       

# """so when we make object like 
# c1 = Atm()
# c2= Atm()
# c3 =Atm()
# >>c1.sno =1
# >>c2.sno = 2
# >>c3.sno =3
# >>c1.counter=4
# >>Atm.Counter =4 
# """


    def get_pin(self):
        return self.__balance

    def set_pin(self, new_pin):
        if type(new_pin)==str:
            self.__pin=new_pin
            print("pin set succesfully")
       
    



    def menu(self):
       option = int(input("""
       Please Press 1-5 button to Proceed further


       1.create_pin
       2.deposit
       3. withdraw
       4. check balance
       5.exit
       """))


       if option ==1:
           self.create_pin()
       elif option ==2:
           self.deposit()
       elif option ==3:
           self.withdraw()
       elif option ==4:
           self.check_balance()
       else:
           print("bye")


    def create_pin(self):
       pint = int(input("Enter Pin"))
       self.__pin =pint
       print("pin created succesfully")


    def deposit(self):
       pint = int(input("Enter Pin"))
       print(self.__pin)
       if self.__pin == pint:
           amount = int(input("enter amount to be deposit"))
           self.__balance = self.__balance+amount
           print("amount deposit successfully")
       else:
           print("invalid Pin")


  
    def withdraw(self):
       pint = int(input("Enter Pin"))
       if self.__pin == pint:
           amount = int(input("enter amount to be withdraw"))
           if amount< self.__balance:
               self.__balance = self.__balance-amount
               print("amount  successfully")
           else:
               print("insufficient balance")
       else:
           print("invalid Pin")
    def check_balance(self):


       pint = int(input("Enter Pin"))
       if self.__pin == pint:
           print(self.__balance)
       else:
           print("invalid Pin")




#static method

class Atm:
    """
   
    
    """
    __counter =1


    def __init__(self):
       self.__balance = 0  #instance variable
       self.__pin =""
       self.sno = Atm.__counter
       Atm.__counter +=1

    


#now by Atm.counter ="hdu" counter value can be changed so we have to make it private and to give access thos e private variable 
# we have to make getter and stter method.

# we make counter to __counter and make 2 sttaic method method
    @staticmethod
    def get_counter():
        return Atm.__counter

    @staticmethod
    def set_counter(new):
        if type(new) == int:
            Atm.__counter = new
        else:
            print("not Allowed")


# so static method are those whoch are accessed without objects and their use is when we are dealing with static variable

    def get_pin(self):
        return self.__balance

    def set_pin(self, new_pin):
        if type(new_pin)==str:
            self.__pin=new_pin
            print("pin set succesfully")



   


