
class Screen(object):
    def __init__(self, thingsInside):
        self.thingsInside = thingsInside

    def checkMouseOver(self):
        for thing in self.thingsInside:
            thing.checkMouseOver()

    def downClick(self):
        for thing in self.thingsInside:
            thing.downClick()

    def upClick(self):
        for thing in self.thingsInside:
            thing.upClick()

    def rescale(self, oldSize=1, newSize=1):
        for thing in self.thingsInside:
            thing.rescale(oldSize, newSize)

    def render(self):
        for thing in self.thingsInside:
            thing.render()
