from resources.screenTools import *

class Screen(object):
    def __init__(self, thingsInside, pos=(0,0), size=(1,1)):
        self.thingsInside = thingsInside
        self.pos = scale(pos)
        self.size = scale(size)
        self.box = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.mouseOver = self.box.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
        # self.surface =

    def isMouseOver(self):
        return self.box.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

    def checkMouseOver(self):
        for thing in self.thingsInside:
            thing.checkMouseOver()

        self.mouseOver = self.isMouseOver()

    def downClick(self):
        for thing in self.thingsInside:
            thing.downClick()

    def upClick(self):
        for thing in self.thingsInside:
            thing.upClick()

    def rescale(self, oldSize, newSize):
        for thing in self.thingsInside:
            thing.rescale(oldSize, newSize)

        self.pos = rescaleForSizeChange(self.pos, oldSize, newSize)
        self.size = rescaleForSizeChange(self.size, oldSize, newSize)

    def render(self, surface):
        for thing in self.thingsInside:
            thing.render(self.surface)
        # pygame.display.update([self.pos[0], self.pos[1], self.size[0], self.size[1]])
