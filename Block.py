import random
import tkinter
from tkinter import *

class entity:
    def __init__(self, spawn, size, colour):
        self.spawn = spawn
        self.size = size
        self.colour = colour

    def move(self):
        x = random.randint(-3,3)
        y = random.randint(-3,3)
        self.spawn[0] += x
        self.spawn[1] += y
        return x,y

    def getSpawn(self):
        return self.spawn

    def getSize(self):
        return self.size

    def getColour(self):
        return self.colour

    def setColour(self, colour):
        self.colour = colour

