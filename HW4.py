# Homework 4
# Prepared by Maksym Bilyi, id: 101169

class Shape:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self._a = a
        self.b = par_b

    def get_a(self):
        return self._a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))

# getting libraries

import math

# setting parameters for a normal triangle
class triangle(Shape):
    def __init__(self,a,b,c):
        Shape.__init__(self, 3)
        self.a = a
        self.b = b
        self.c = c

# defining a function that calculates area
    def area(self):
        s = (self.a + self.b + self.c) / 2
        area = math.sqrt(s * ((s - self.a) * (s - self.b) * (s - self.c)))
        return area

# defining a function that calculates perimeter
    def perimeter(self):
        return self.a + self.b + self.c

# printing results for a normal triangle
    t=triangle(5,3,5)
    print(t) ### output triangle[3 by 3] at 0x7f989954abb0
    print(t.perimeter())  ### output 13
    print(t.area()) ### output 7.1545440106270926

# check if numbers can actually create a triangle
def checkforT(a, b, c):
    if a + b<= c or b + c<= a or c + a<= b:
        return print("FALSE")
    else: print("TRUE")

print(checkforT(5,3,5)) ### output TRUE for 5,3,5

# setting parameters for Equitriangle

class EquiTriangle(triangle):
    def __init__(self, a):
        b = a
        c = a
        super().__init__(a, b, c)

    def area(self):
        area = math.sqrt(3) * pow(self.a, 2) / 4
        return area
    def perimeter(self):
        return self.a + self.b + self.c

# printing results

et = EquiTriangle(10)
print(et) ### output EquiTriangle[3 by 10] at 0x7f989956a3d0
print(et.perimeter())  ### output 20
print(et.area()) ### output 43.30127018922193