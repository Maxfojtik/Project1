from screenTools import *
import sprite
from colors import *

class switch(sprite.Sprite):

    def __init__(self, pos, size, border="auto", bevel="auto"):
        self.pos = scale(pos)
        self.size = scale(size)
        self.box = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.state = False # TODO: Make this be set by the variable
        self.sliderPos = 0 # The position it is, not where it is headed toward

        if border == "auto":
            border = (self.size[1]-(2**.5 * self.border))/2
        else:
            border *= size[0]  # Scale the bevel for the screen
        self.bevel = min(min(self.size[1]/2, self.size[0]/2), border)  # Makes sure that the border makes sense

        if bevel == "auto":
            bevel = (self.size[1]-(2**.5 * self.border))/2
        else:
            bevel *= size[0]  # Scale the bevel for the screen
        self.bevel = min(min(self.size[1]/2, self.size[0]/2), bevel)  # Makes sure that the bevel is less than the sides


    def onClick(self):
        self.state = not self.state

    def render(self):

        pygame.draw.polygon(self.surface, BLACK,getPoly(self.pos,self.size,self.bevel))