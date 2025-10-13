import math
class Rectangle:
    def __init__ (self,width,height):
        self.width=width
        self.height=height
    def get_square(self):
        return self.width*self.height
    def __eq__(self,other):
        if isinstance(other,Rectangle):
            return abs(self.get_square() - other.get_square()) < 1e-6
        return NotImplemented
    def __add__(self,other):
        if isinstance(other,Rectangle):
            new_square=self.get_square()+other.get_square()
            ratio=self.width/self.height
            new_height=math.sqrt(new_square/ratio)
            new_width = new_height * ratio
            return Rectangle(new_width,new_height)
        return NotImplemented
    def __mul__(self,other):
        if isinstance(other,(int,float)):
            new_square=self.get_square()*other
            ratio = self.width / self.height
            new_height=math.sqrt(new_square/ratio)
            new_width = new_height * ratio
            return Rectangle(new_width,new_height)
        return NotImplemented
    def __str__(self):
        return f'Rectangle(width={self.width:.2f}, height={self.height:.2f}, area={self.get_square():.2f})'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)

assert abs(r1.get_square() - 8) < 1e-6, 'Test1'
assert abs(r2.get_square() - 18) < 1e-6, 'Test2'

r3 = r1 + r2
assert abs(r3.get_square() - 26) < 1e-6, 'Test3'

r4 = r1 * 4
assert abs(r4.get_square() - 32) < 1e-6, 'Test4'

assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
print("ok")

