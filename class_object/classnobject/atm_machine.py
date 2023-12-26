class Atm:

    """__init__: it is a constructor is a special method which 
    is automatically called when object of the class is created. 
    It is a magic method/ dunder method. The control of init is not
     performed by user."""

    def __init__(self):
       self.balance = 0 
    #    instance variable : variable which are written inside __int__. it is a variable for which
    # the vaule of variable is different for different object
       self.pin =""

       self.menu()
       print(id(self))
       """In oops in a class there can be only data and methods . 
        and they can be accessed through only by its object.
        method inside a class cannot communicate with other methods directly. 
        They can access other methods through objects only. That's why self is used 
        as it is current object
        when you create a object of this class sbi = Atm()
        id(sbi) is equal to id(self)
        """



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
       self.pin =pint
       print("pin created succesfully")


    def deposit(self):
       pint = int(input("Enter Pin"))
       print(self.pin)
       if self.pin == pint:
           amount = int(input("enter amount to be deposit"))
           self.balance = self.balance+amount
           print("amount deposit successfully")
       else:
           print("invalid Pin")


  
    def withdraw(self):
       pint = int(input("Enter Pin"))
       if self.pin == pint:
           amount = int(input("enter amount to be withdraw"))
           if amount< self.balance:
               self.balance = self.balance-amount
               print("amount  successfully")
           else:
               print("insufficient balance")
       else:
           print("invalid Pin")
    def check_balance(self):


       pint = int(input("Enter Pin"))
       if self.pin == pint:
           print(self.balance)
       else:
           print("invalid Pin")
