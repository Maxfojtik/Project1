
class Screen(object):
    def __init__(self, buttons):
        self.buttons = buttons

    def checkMouseOver(self):
        for button in self.buttons:
            button.checkMouseOver()

    def downClick(self):
        for button in self.buttons:
            button.downClick()

    def upClick(self):
        for button in self.buttons:
            button.upClick()

    def rescale(self, oldSize=1, newSize=1):
        for button in self.buttons:
            button.rescale(oldSize, newSize)

    def render(self):
        for button in self.buttons:
            button.render()
