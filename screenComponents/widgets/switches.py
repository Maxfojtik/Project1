from resources.screenTools import *
from screenComponents.widgets import widget
from resources.colors import *

class Switch(widget.Widget):

    def __init__(self, pos, size, buttonWidth="auto", border="auto", bevel="auto"):
        assert 0 <= pos[0] < 1 and 0 <= pos[1] < 1
        assert 0 <= size[0] <= 1 and 0 <= size[1] <= 1
        assert size[0] + pos[0] <= 1 and size[1] + pos[1] <= 1

        self.pos = scale(pos)
        self.size = scale(size)
        self.box = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.state = False # TODO: Make this be set by the variable
        self.sliderPos = 0 # The position it is, not where it is headed toward

        self.surface = pygame.display.get_surface()

        if border == "auto":
            border = diagonal(self.size)/25
        else:
            border *= size[0]  # Scale the bevel for the screen
        self.border = min(min(self.size[1]/2, self.size[0]/2), border)  # Makes sure that the border makes sense

        if buttonWidth == "auto":
            buttonWidth = (self.size[0]-self.border*2)/1.6
        else:
            buttonWidth *= size[0]
        self.buttonWidth = buttonWidth

        if bevel == "auto":
            bevel = diagonal(self.size)/12
        else:
            bevel *= size[0]  # Scale the bevel for the screen
        self.bevel = min(min(self.size[1]/2, self.size[0]/2), bevel)  # Makes sure that the bevel is less than the sides


    def onClick(self):
        self.state = not self.state

    def rescale(self, oldSize, newSize):
        self.pos = rescaleForSizeChange(self.pos, oldSize, newSize)
        self.size = rescaleForSizeChange(self.size, oldSize, newSize)
        self.bevel = rescaleForSizeChange(self.bevel, oldSize, newSize)

    def render(self):

        pygame.draw.polygon(self.surface, BLACK,getPoly(self.pos,self.size,self.bevel))

        pygame.draw.polygon(self.surface, DARK_BLUE, getPoly(
            (self.pos[0] + self.border, self.pos[1] + self.border), (self.size[0] - self.border * 2, self.size[1] - self.border * 2), self.bevel - self.border / 2**.5))

        # Switch is to the right (on)
        if self.state:
            pygame.draw.polygon(self.surface, WHITE, getPoly(
                (self.pos[0] + self.size[0] - self.border - self.buttonWidth, self.pos[1] + self.border),
                (self.buttonWidth, self.size[1] - self.border*2), self.bevel - self.border / 2**.5))

        # Switch is to the left (off)
        else:
            pygame.draw.polygon(self.surface, WHITE, getPoly(
                (self.pos[0] + self.border, self.pos[1] + self.border), (self.buttonWidth, self.size[1] - self.border * 2), self.bevel - self.border / 2**.5))


