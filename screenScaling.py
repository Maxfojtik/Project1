import pygame

def scale(num):
    for i in num:
        assert i<=1
    screenSize = pygame.display.get_surface().get_size()
    return [num[i] * screenSize[i] for i in range(0, len(num))]