from screenTools import *

class Sprite(object):

    def isMouseOver(self):
        return self.box.collidepoint(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1])

    def checkMouseOver(self):
        self.mouseOver = self.isMouseOver()

    def downClick(self):
        # Down click is here because buttons should only activate if you click down then up on them
        self.downClicked = self.isMouseOver()

    def upClick(self):
        if self.downClicked and self.isMouseOver():
            self.onClick()
        self.downClicked = False

    def render(self):
        raise Exception("sprite's render function should not be called, make one for each class")

    def rescale(self):
        raise Exception("sprite's rescale function should not be called, make one for each class")
