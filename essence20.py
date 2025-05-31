from math import ceil
from random import random
from enum import IntEnum

class DiceLadder(IntEnum):
    UNTRAINED = 0
    d2 = 1
    d4 = 2
    d6 = 3
    d8 = 4
    d10 = 5
    d12 = 6
    twod8 = 7
    threed6 = 8
    def __str__(self):
        if self.name == "twod8":
            return "2d8"
        elif self.name == "threed6":
            return "3d6"
        else:
            return self.name

def roll(a):
    return ceil(random()*a)

def d20portion(edge, v) -> int:
    d20 = roll(20)
    if edge != 0:
        secondd20 = roll(20)
        if v:
            v.append20(d20,secondd20)
        value = max(d20,secondd20) if edge > 0 else min(d20,secondd20)
    else:
        if v:
            v.append20(d20)
        value = d20
    return value

def skilldieportion(skilldie, specialized, v) -> int:
    if skilldie not in DiceLadder:
        raise TypeError(str(skilldie) + " not on the ladder, come on bro")
    if skilldie == DiceLadder.UNTRAINED:
        return 0
    
    if skilldie == DiceLadder.threed6:
        value = roll(6)+roll(6)+roll(6)
    elif skilldie == DiceLadder.twod8:
        value = roll(8)+roll(8)
    else:
        value = roll(skilldie*2)

    if v:
        v.appendskill(skilldie, value)
    
    if specialized:
        value = max(value, skilldieportion(DiceLadder(skilldie-1), specialized, v))
        
    return value
    

def check(skilldie: DiceLadder, specialized: bool, edge: int, verbose: bool) -> int:
    if verbose:
        v = VerbosePrinter(skilldie, specialized, edge)
    else:
        v = None
    d20 = d20portion(edge, v)
    skilldie = skilldieportion(skilldie,specialized, v)

    if v:
        v.appendtotal(d20, skilldie)
        print(v)

    return d20 + skilldie

class VerbosePrinter:
    def __init__(self, skilldie, specialized, edge):
        self.s = "Roll with " + str(skilldie)
        if specialized:
            self.s += "*"
        if edge>0:
            self.s += " (Edge)"
        elif edge<0:
            self.s += " (Snag)"
        self.s += ": "

    def append20(self, val1, val2=None):
        self.s += "d20: "
        if val2:
            self.s += str(val1) + ", " + str(val2)
        else:
            self.s += str(val1)
        self.s += " "

    def appendskill(self, skilldie, val):
        self.s += str(skilldie) + ": " + str(val) + " "

    def appendtotal(self, d20val, skillval):
        self.s += "Total: " + str(d20val) + " + " + str(skillval) + " = " + str(d20val+skillval)
        
    def __str__(self):
        return self.s
