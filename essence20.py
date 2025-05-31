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

def roll(a):
    return ceil(random()*a)

def d20portion(edge) -> int:
    d20 = roll(20)
    secondd20 = roll(20)
    return max(d20,secondd20) if edge > 0 else (min(d20,secondd20) if edge < 0 else d20)

def skilldieportion(skilldie, specialized) -> int:
    if skilldie not in DiceLadder:
        raise TypeError(str(skilldie) + " not on the ladder, come on bro")
    if skilldie == DiceLadder.UNTRAINED:
        return value
    value = 0
    elif skilldie == DiceLadder.threed6:
        value = roll(6)+roll(6)+roll(6)
    elif skilldie == DiceLadder.twod8:
        value = roll(8)+roll(8)
    else:
        value = roll(skilldie*2)

    if specialized:
        value = max(value, skilldieportion(DiceLadder(skilldie-1), specialized))

    return value
    

def check(skilldie, specialized=False, edge=0) -> int:
    d20 = d20portion(edge)
    skilldie = skilldieportion(skilldie,specialized)
    return d20 + skilldie
