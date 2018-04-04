import pygame

def scale(num):
    for i in num:
        assert i<=1
    screenSize = pygame.display.get_surface().get_size()
    return [num[i] * screenSize[i] for i in range(0, len(num))]

def rescaleForSizeChange(num, oldSize, newSize):
    if type(num)==type(1) or type(num)==type(.5):
        return num * (((newSize[0]**2 + newSize[1]**2)**.5) / ((oldSize[0]**2 + oldSize[1]**2)**.5))
    else:
        return [num[i] * (newSize[i] / oldSize[i]) for i in range(0, len(num))]
