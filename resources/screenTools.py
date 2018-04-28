import pygame

def scale(num):
    screenSize = pygame.display.get_surface().get_size()
    if type(num)==type(1) or type(num)==type(.5): # If num is one number
        assert num <= 1
        return int(num * diagonal(screenSize))
    else: # If it is an array of two numbers
        for i in num:
            assert i<=1
        return [int(num[i] * screenSize[i]) for i in range(0, len(num))]

def scaleOrDefault(num, default, cap=None):
    val = default
    if num != "auto":
        val = scale(num)
    if cap and default != "auto":
        val = max(cap[0], min(cap[1], val))
    return val

def rescaleForSizeChange(num, oldSize, newSize): # Scale num to be the same relative to the new size
    if oldSize == newSize: # If there is no screen size, don't waste processing power
        return num
    elif type(num)==type(1) or type(num)==type(.5): # If num is one number
        return num * (diagonal(newSize) / diagonal(oldSize))
    else: # If num is an array or tuple (assumed to be size 2
        return [num[i] * (newSize[i] / oldSize[i]) for i in range(0, len(num))]

def getPoly(pos, size, bevel): # Construct an octagon with given position, size, and bevel
    rightX = pos[0] + size[0]
    botY = pos[1] + size[1]
    return [[pos[0] + bevel, pos[1]], [rightX - bevel, pos[1]], [rightX, pos[1] + bevel], [rightX, botY - bevel],
     [rightX - bevel, botY], [pos[0] + bevel, botY], [pos[0], botY - bevel], [pos[0], pos[1] + bevel]]

def diagonal(x,y=None): # Pythagorean distance, either for two numbers or one array with two numbers
    if y: # Two numbers
        return (x**2+y**2)**.5
    else: # X is a size 2 array or tuple
        return (x[0]**2+x[1]**2)**.5
