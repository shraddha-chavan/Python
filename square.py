import math

class Position:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def distance(self):
        return math.sqrt(self.x**2 + self.y**2)

p1 = Position(3, 5)

Distance= p1.distance()
print(Distance)
