"""encapsulation
private variable
instance variable
getter and setter method


"""

class Customer:
    """suppose 
    sbi = Atm()
    sbi.__balance ="hgshdghg"
    this way we can change the balance and on calling sbi.deposit() method we will get
    a error(attribute error str + int not allowed )so in python we should keep our 
    data inaccesible to User by making private by appendin __
   
    
    """


    def __init__(self):
       self.__balance = 0 # this is now a priavte variable which in memory is denoted by _Atm__balance so if user 
       #set value of sbi.__balance =="ytyt" and tries to call sbi.withdraw .. it willnot  give error asin memory a
       #  seperate variable with a __balance is created and its value is updated to "ytyt".
       
       self.__pin =""

       #as user is now unable to access to the data memeber of the class as we have make them provate , so if we
       #  want to give user a faeature to access these we can use setter and getter method

       self.menu()

    def get_pin(self):
        return self.__pin

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


#so encapsulation here is done by making data memeber private and then allow user to access and set data memeber
#  by getter and setter method. so this is encapsulation.
#so first rule is that we should hide our data member. as some one change the data memeber
#  so data +getter and setter method is encapsultion