"""
1. method overloading : in which  in a single class we  have two method with same name but have diffrent behaviour 
for different input
2. method overriding : inheritane when same child class and parent class have same method name then child
class method will be executed
3. opertor  overloading : same operatot is diffrent for diffrent input
"""


#Polymorphism: having sevareal phases, same thing react differently for different input



# 1. method overloading : in which  in a single class we  have two method with same name but have diffrent behaviour 
# for different input 

# uses: we get clean code in python there is no method overloading
class Shape:

    def area(self, radius):
        return 3.14 *radius * radius


    def area(self,l,b):
        return l*b

s = Shape()
# s.area(2) # python will take 2 area method infact we have methid overloading by using default arguement
# s.area(10,20)


class Shape:

    def area(self, a,b=0):
        if b ==0:
            return 3.14 * a*a

        else :
            return a*b



s = Shape()
print(s.area(2))
print(s.area(10,20))

# operator overloading

print( 'hello ' + 'world')
print(7+8)
print([6,7]+[9,3])

# in all three example operator is same but action is different for different values