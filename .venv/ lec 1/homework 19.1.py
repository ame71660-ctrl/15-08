import math
class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник не може бути нулем")
        self.a=a
        self.b=b
        self.reduce()
    def reduce(self):
        import math
        gcd = math.gcd(self.a, self.b)
        self.a //= gcd
        self.b //= gcd
    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.a*other.a, self.b*other.b)
        return NotImplemented
    def __add__(self, other):
        if isinstance(other, Fraction):
            new_a=self.a*other.b+self.b*other.a
            new_b=self.b*other.b
            return Fraction(new_a, new_b)
        return NotImplemented
    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_a=self.a * other.b - self.b * other.a
            new_b=self.b * other.b
            return Fraction(new_a, new_b)
        return NotImplemented
    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b == self.b * other.a
        return NotImplemented
    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b > self.b * other.a
        return NotImplemented
    def __lt__ (self, other):
        if isinstance(other, Fraction):
            return self.a * other.b < self.b * other.a
        return NotImplemented
    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
f_d = f_b * f_a
f_e = f_a - f_b

assert str(f_c) == 'Fraction: 7, 6'
assert str(f_d) == 'Fraction: 1, 3'
assert str(f_e) == 'Fraction: 1, 6'

assert f_d < f_c
assert f_d > f_e
assert f_a != f_b

f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2

print('OK')



