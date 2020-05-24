import random
import tkinter
from tkinter import *

class entity:
    def __init__(self, spawn, size, colour):
        self.spawn = spawn
        self.size = size
        self.colour = colour
        self.target = spawn
        self.timeInfected = 0

    def genTarget(self, canvasSize):
        target = [0,0]
        target[0] = random.randint(0, canvasSize-10)
        target[1] = random.randint(0, canvasSize-10)
        return target

    def move(self, canvasSize):
        x = 0
        y = 0
        if self.spawn[0] == self.target[0] and self.spawn[1] == self.target[1]:
            self.target = self.genTarget(canvasSize)
        if self.spawn[0] > self.target[0]:
            x = -1
            self.spawn[0] += -1
        if self.spawn[0] < self.target[0]:
            x = 1
            self.spawn[0] += 1
        if self.spawn[1] > self.target[1]:
            y = -1
            self.spawn[1] += -1
        if self.spawn[1] < self.target[1]:
            y = 1
            self.spawn[1] += 1

        return x,y

    def getSpawn(self):
        return self.spawn

    def setTimeInfected(self):
        self.timeInfected +=1

    def getSize(self):
        return self.size

    def getColour(self):
        return self.colour

    def setColour(self, colour):
        self.colour = colour

