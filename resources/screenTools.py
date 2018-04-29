import pygame

# Scales the number or array from between 0-1 to 0-screen size, based off the screen size
def scale(num):
    screenSize = pygame.display.get_surface().get_size()
    if type(num)==type(1) or type(num)==type(.5): # If num is one number
        assert num <= 1
        return int(num * diagonal(screenSize))
    else: # If it is an array of two numbers
        for i in num:
            assert i<=1
        return [int(num[i] * screenSize[i]) for i in range(0, len(num))]

# Scale but also allows capping, and setting from a default if num is "auto"
def scaleOrDefault(num, default, cap=None):
    val = default
    if num != "auto": # If you have a value you want instead of the default
        val = scale(num)
    if cap and default != "auto":
        val = max(cap[0], min(cap[1], val))
    return val

# When the screen is resized, this helps scale based on the new and old size of the screen
def rescaleForSizeChange(num, oldSize, newSize):
    if oldSize == newSize: # If there is no screen size, don't waste processing power
        return num
    elif type(num)==type(1) or type(num)==type(.5): # If num is one number
        return num * (diagonal(newSize) / diagonal(oldSize))
    else: # If num is an array or tuple (assumed to be size 2
        return [num[i] * (newSize[i] / oldSize[i]) for i in range(0, len(num))]

# Construct an octagon with given position, size, and bevel
def getPoly(pos, size, bevel):
    rightX = pos[0] + size[0]
    botY = pos[1] + size[1]
    return [[pos[0] + bevel, pos[1]], [rightX - bevel, pos[1]], [rightX, pos[1] + bevel], [rightX, botY - bevel],
     [rightX - bevel, botY], [pos[0] + bevel, botY], [pos[0], botY - bevel], [pos[0], pos[1] + bevel]]

# Pythagorean distance, either for two numbers or one array with two numbers
def diagonal(x,y=None):
    if y: # Two numbers
        return (x**2+y**2)**.5
    else: # X is a size 2 array or tuple
        return (x[0]**2+x[1]**2)**.5
