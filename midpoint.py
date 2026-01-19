import math

class Position:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def midpoint(self, p2):
        mx = (self.x + p2.x) / 2
        my = (self.y + p2.y) / 2
        return Position(mx, my)

p1 = Position(2, 4)
p2 = Position(6, 8)

p3 = p1.midpoint(p2)

print("Midpoint is:", p3.x, p3.y)
