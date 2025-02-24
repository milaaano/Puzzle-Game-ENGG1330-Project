# INSTRUCTIONS
# 1.    Instantiation
#       To instantiate a Vector, call Vector(x1, x2, ...) or Vector(<tuple>)
# 2.    Conversion
#       To retrieve a tuple from a Vector, call <Vector>.value or <Vector>.to_tuple()
# 3.    Applications
#       - Basic arithmatics
#       - .x, .y to get x-coords and y-coords
#       For more methods check source code.
# Feel free to run the test below.
# That's all!

import math

class Vector:

    def __init__(self, *value):
        first = value[0]
        if type(first) == Vector:
            # Copy constructor.
            self.value = first.value
        elif type(first) == tuple:
            # Parameter is a tuple wrapped inside another tuple.
            self.value = first
        else:
            self.value = value
    
    def __add__(self, other):
        new_value = ()
        for x, y in zip(self.value, other.value):
            new_value += x + y,
        return Vector(new_value)
    
    def __sub__(self, other):
        return self + -other

    def __neg__(self):
        return Vector(tuple(map(lambda x : -x, self.value)))
    
    def __mul__(self, scalar):
        def mul(x):
            nonlocal scalar
            return x * scalar
        return Vector(tuple(map(mul, self.value)))

    def to_tuple(self) -> tuple:
        return self.value

    # x-coordinate.
    @property
    def x(self):
        return self.value[0]

    @x.setter
    def x(self, value):
        self.value[0] = value
    
    # y-coordinate.
    @property
    def y(self):
        return self.value[1]

    @y.setter
    def y(self, value):
        self.value[1] = value
    
    # returns magnitude.
    def mag(self):
        return math.sqrt(sum(map(lambda x : x**2, self.value)))

    # returns a normalized version of the vector. (magnitude = 1)
    def normalized(self):
        return self * (1 / self.mag())

# returns a (2D) direction.
def direction(d) -> Vector:
    match d:
        case 'u':
            return Vector(0, -1)
        case 'd':
            return Vector(0, 1)
        case 'l':
            return Vector(-1, 0)
        case 'r':
            return Vector(1, 0)
        case _:
            return Vector.zero(2)

# returns zero vector.
def zero(dim: int):
    return Vector(tuple(0 for i in range(dim)))

# returns distance between v1 and v2.
def dist(v1: Vector, v2: Vector):
    return (v1 - v2).mag()
