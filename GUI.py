import tkinter
import Block as b
from tkinter import *
import time
import random
sec = 0.1
root = Tk()

class canvas:
    global Cav
    Cav = Canvas(root, width=1000, height=1000)
    Cav.pack()

    def update(self):
        root.update()

    def moveBlock(self, block, x, y):
        Cav.move(block, x, y)


    ent = b.entity
    rect =0


C = canvas()


cubeys = []
for i in range(0,1000):
    if i == 1:
        cubey = {"ent": b.entity([random.randint(50, 950), random.randint(50, 950)], 10, "RED")}
        rect = Cav.create_rectangle(cubey["ent"].getSpawn()[0], cubey["ent"].getSpawn()[1],
                                    cubey["ent"].getSpawn()[0] + cubey["ent"].getSize(),
                                    cubey["ent"].getSpawn()[1] + cubey["ent"].getSize(), fill=cubey["ent"].getColour())

    else:
        cubey = {"ent": b.entity([random.randint(50, 950), random.randint(50, 950)], 10, "GREEN")}
        rect = Cav.create_rectangle(cubey["ent"].getSpawn()[0], cubey["ent"].getSpawn()[1],
                                    cubey["ent"].getSpawn()[0] + cubey["ent"].getSize(),
                                    cubey["ent"].getSpawn()[1] + cubey["ent"].getSize(), fill=cubey["ent"].getColour())
    cubey["rect"] = rect
    cubeys.append(cubey)

    C.update()

print(cubeys)

while True:
    for X in cubeys:
        x ,y = X["ent"].move()
        C.moveBlock(X["rect"], x, y)

        if X["ent"].getColour() == "RED":
            for I in cubeys:
                if I["ent"].getColour() != "RED":
                    if X["ent"].getSpawn()[0] >= I["ent"].getSpawn()[0]-10 and X["ent"].getSpawn()[0] <= I["ent"].getSpawn()[0] +10:
                        if X["ent"].getSpawn()[1] >= I["ent"].getSpawn()[1]-10 and X["ent"].getSpawn()[1] <= I["ent"].getSpawn()[1] +10:
                            I["ent"].setColour("RED")
                            Cav.itemconfig(I["rect"], fill = "RED")

    root.update()

root.mainloop()