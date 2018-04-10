from screenTools import *

class ScrollView:

    def __init__(self, content, pos, size):
        self.content = content
        self.pos = scale(pos)
        self.size = scale(size)
        self.box = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.mouseOver = self.box.collidepoint(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])

    def isMouseOver(self):
        return self.box.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

    def checkMouseOver(self):
        for thing in self.content:
            thing.checkMouseOver()

        self.mouseOver = self.isMouseOver()

    def downClick(self):
        for thing in self.content:
            thing.downClick()

    def upClick(self):
        for thing in self.content:
            thing.upClick()

    def rescale(self, oldSize, newSize): # for when the window is changed to a different size
        for thing in self.content:
            thing.rescale(oldSize, newSize)

        self.pos = rescaleForSizeChange(self.pos, oldSize, newSize)
        self.size = rescaleForSizeChange(self.size, oldSize, newSize)

    def render(self):
        for thing in self.content:
            pass