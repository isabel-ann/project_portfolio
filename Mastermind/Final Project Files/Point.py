'''
CS 5001 
Isabel Cuddihy
Final Project - Mastermind Class (Point)
12-08-2023
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def delta_x(self, other):
        return abs(self.x - other.x)

    def delta_y(self, other):
        return abs(self.y - other.y)