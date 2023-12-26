"""
1. a user can view and create 2d cordinates
2. user can find the distance between the 2 cordinates
3. user can distane of cordinate from origin
4.  a user can  if a given point lies in given line
5. user can find the distace between two ponits and a line
6 . whether two given line intersect ot not.
"""

class Point():

    def __init__(self, x, y):
        self.x_cod = x
        self.y_cod = y

    
    def __str__(self):
       return("<{},{}>".format(self.x_cod,self.y_cod))

    def eculidean_distance(self,other):
        return (((self.x_cod-other.x_cod)**2) +((self.y_cod - other.y_cod)**2))**.5

    def distance_from_origin(self):
        return self.eculidean_distance(Point(0,0))



p = Point(0,0) # a user can view and create 2d cordinates
p2 =Point(1,1)# a user can view and create 2d cordinates
print(p) # a user can view and create 2d cordinates
print(p2) # a user can view and create 2d cordinates
print(p.eculidean_distance(p2)) #2. user can find the distance between the 2 cordinates
print(p2.distance_from_origin()) #3. user can distane of cordinate from origin


class Line():

    def __init__(self,a,b,c):
        self.a =a
        self.b = b
        self.c = c

    def __str__(self):
        return ("{}x + {}y + {}c = 0".format(self.a,self.b,self.c))

    def point_lies_on_line(line,point):
        
        if line.a * point.x_cod + line.b*point.y_cod + line.c ==0:
            return "lies on line"
        else:
            return "doesnot lies on line"

    def shortest_distance(line,point):
        return abs(line.a * point.x_cod + line.b*point.y_cod + line.c) / (line.a **2 + line.b**2) **.5

    def line_intersect(self, other):
        

k = Line(1,1,-2)
m = Line(2,3,5)
l = Point(1,1)
print(k.point_lies_on_line(l)) #4.  a user can  if a given point lies in given line
print(k.shortest_distance(l))
