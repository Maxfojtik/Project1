from screenScaling import *
from colors import *

class Slider(object):

    def __init__(self, pos, size, sliderSize, bounds, showNumber = True):
        self.pos = scale(pos)
        self.size = scale(size)
        self.sliderSize = scale(sliderSize)
        self.bounds = bounds # The lower and upper possible values for the number set by the slider
        self.sliderPos = .3 # TODO make this be set from an actual value (map to percentage)
        self.showNumber = showNumber # Whether or not to show the current value
        self.sliderBox = pygame.Rect(self.pos[0] + self.size[0]*self.sliderPos - (self.sliderSize[0] / 2),
                                     self.pos[1] + (self.size[1] - self.sliderSize[1]) / 2, self.sliderSize[0], self.sliderSize[1])
        self.box = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1]) # The rectangle of the entire slider
        self.surface = pygame.display.get_surface()
        self.mouseOver = False # Keeps track of if the button is being moused over
        self.downClicked = False # Keeps track of whether you clicked on the button but have not yet released
        self.posOff = 0 # If you click on it, but slightly off, it saves the amount you are off so that it doesn't jump the slider to your mouse

        assert pos[0]<=1 and pos[1]<=1
        assert size[0]<=1 and size[1]<=1
        assert 1>=self.sliderPos>=0

    def isMouseOver(self): # Return whether or not the mouse is over the slider
        return self.box.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    def checkMouseOver(self): # Do mouse over stuff, such as checking if the mouse is over the slider
        if self.downClicked:
            self.sliderPos = (pygame.mouse.get_pos()[0] - self.pos[0]) / self.size[0] - self.posOff
            self.sliderPos = max(0,min(1,self.sliderPos)) # Clip value to be within range
        self.mouseOver = self.isMouseOver()
        return self.mouseOver

    def downClick(self):
        self.downClicked = self.isMouseOver()
        if self.sliderBox.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]):
            self.posOff = 0 # TODO correct this
        else:
            self.posOff = 0

    def upClick(self):
        if self.downClicked:
            pass # self.onClick() # TODO make this change a variable value, hopefully in an easier way than needing a function for every slider
        self.downClicked = False

    def rescale(self, oldSize, newSize):
        self.pos = rescaleForSizeChange(self.pos, oldSize, newSize)
        self.size = rescaleForSizeChange(self.size, oldSize, newSize)
        self.sliderSize = rescaleForSizeChange(self.sliderSize, oldSize, newSize)

    def render(self):

        pygame.draw.rect(self.surface, BLACK, [self.pos[0], self.pos[1], self.size[0], self.size[1]])

        self.sliderBox = pygame.draw.rect(self.surface, DARK_BLUE, [self.pos[0] + self.size[0]*self.sliderPos - (self.sliderSize[0] / 2),
                                                   self.pos[1] + (self.size[1] - self.sliderSize[1]) / 2, self.sliderSize[0], self.sliderSize[1]])

