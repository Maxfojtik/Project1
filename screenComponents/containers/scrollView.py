from screenComponents.containers.screen import Screen
import pygame

class ScrollView(Screen):

    def __init__(self, thingsInside, pos, size):
        Screen.__init__(self, thingsInside, pos, size)

    def render(self):
        for thing in self.thingsInside:
            thing.render()
        # pygame.display.update([self.pos[0], self.pos[1], self.size[0], self.size[1]])