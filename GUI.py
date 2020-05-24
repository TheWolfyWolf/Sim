import tkinter
import Block as b
from tkinter import *
import time
import random
root = Tk()

"""Variables"""
population = 1000
sec = 0.1
cavasSize = 1000

""""""

"""GUI"""
class canvas:
    global Cav
    frame = Frame(root, width=300, height=300)
    frame.pack(expand=True, fill=BOTH)  # .grid(row=0,column=0)
    Cav = Canvas(frame, bg='#FFFFFF', width=cavasSize, height=cavasSize, scrollregion=(0, 0, cavasSize, cavasSize))
    hbar = Scrollbar(frame, orient=HORIZONTAL)
    hbar.pack(side=BOTTOM, fill=X)
    hbar.config(command=Cav.xview)
    vbar = Scrollbar(frame, orient=VERTICAL)
    vbar.pack(side=RIGHT, fill=Y)
    vbar.config(command=Cav.yview)
    Cav.config(width=300, height=300)
    Cav.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
    Cav.pack(side=LEFT, expand=True, fill=BOTH)

    def update(self):
        root.update()

    def moveBlock(self, block, x, y):`
        Cav.move(block, x, y)

C = canvas()
Legends = StringVar()
Legend = tkinter.Label(root, textvariable =Legends).pack()

def updateLegend(pop,infected):
    texty = "Population = ", pop, "  Active Infected =  ", infected
    Legends.set(texty)
    root.update_idletasks()

""""""

"""Generator"""
ent = b.entity
rect =0
cubeys = []
badCubeys = []
for i in range(0,population):
    if i == 0:
        cubey = {"ent": b.entity([random.randint(10, cavasSize-10), random.randint(10, cavasSize-10)], 10, "BLUE")}
        rect = Cav.create_rectangle(cubey["ent"].getSpawn()[0], cubey["ent"].getSpawn()[1],
                                    cubey["ent"].getSpawn()[0] + cubey["ent"].getSize(),
                                    cubey["ent"].getSpawn()[1] + cubey["ent"].getSize(), fill=cubey["ent"].getColour())
        cubey["rect"] = rect
        badCubeys.append(cubey)
        print(cubey["ent"].getSpawn())

    else:
        cubey = {"ent": b.entity([random.randint(10, cavasSize-10), random.randint(10, cavasSize-10)], 10, "GREEN")}
        rect = Cav.create_rectangle(cubey["ent"].getSpawn()[0], cubey["ent"].getSpawn()[1],
                                    cubey["ent"].getSpawn()[0] + cubey["ent"].getSize(),
                                    cubey["ent"].getSpawn()[1] + cubey["ent"].getSize(), fill=cubey["ent"].getColour())
        cubey["rect"] = rect
    cubeys.append(cubey)
""""""

"""Main Loop"""
while True:
    for X in cubeys:
        x ,y = X["ent"].move(cavasSize)
        C.moveBlock(X["rect"], x, y)

        if X["ent"].getColour() == "RED" or X["ent"].getColour() == "BLUE":
            X["ent"].setTimeInfected()
        if X["ent"].timeInfected >= 10:
            Cav.delete(X["rect"])

        if X["ent"].getColour() != "RED" and X["ent"].getColour() != "BLUE":
            for I in badCubeys:
                if I["ent"].getSpawn()[0] >= X["ent"].getSpawn()[0]-10 and I["ent"].getSpawn()[0] <= X["ent"].getSpawn()[0] +10 and I["ent"].getSpawn()[1] >= X["ent"].getSpawn()[1]-10 and I["ent"].getSpawn()[1] <= X["ent"].getSpawn()[1] +10:
                        X["ent"].setColour("RED")
                        Cav.itemconfig(X["rect"], fill = "RED")
            if X["ent"].getColour() == "RED":
                badCubeys.append(X)

    updateLegend(population, len(badCubeys))
    C.update()
""""""



