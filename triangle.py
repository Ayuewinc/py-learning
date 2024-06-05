from math import sqrt

class Triangle(object):
    def __init__(self, a ,b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) *
                    (half - self._b) * (half - self._c))

if __name__ == '__main__':
    a, b, c = map(int, input("Please input:").split())
    if Triangle.is_valid(a, b, c):
        triangle = Triangle(a, b, c)
        print(triangle.perimeter())
        print(triangle.area())
    else:
        print("That's not a triangle")