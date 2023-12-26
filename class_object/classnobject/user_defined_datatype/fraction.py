# Create your Dtatatype


class Fraction:
# dir(int) to get magic method

   def __init__(self, num, deno):
       self.num = num
       self.deno = deno


   def __str__(self):
       return("{}/{}".format(self.num,self.deno))


   def __add__(self, other):
       temp_num = self.num * other.deno + self.deno * other.num
       temp_deno = self.deno * other.deno
       return("{}/{}".format(temp_num,temp_deno))


  
   def __sub__(self, other):
       temp_num = self.num * other.deno - self.deno * other.num
       temp_deno = self.deno * other.deno
       return("{}/{}".format(temp_num,temp_deno))


  
   def __mul__(self, other):
       temp_num = self.num * other.num
       temp_deno = self.deno * other.deno
       return("{}/{}".format(temp_num,temp_deno))


  
   def __truediv__(self, other):
       temp_num = self.num * other.deno
       temp_deno = self.deno * other.num
       return("{}/{}".format(temp_num,temp_deno))


obj = Fraction(5,6)
ob2 = Fraction(1,2)


print(obj)
print(ob2)
print(obj + ob2)
print(obj - ob2)
print(obj * ob2)
print(obj / ob2)                      

