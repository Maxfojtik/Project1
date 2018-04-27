from resources.colors import *
from resources.screenTools import *
from screenComponents.widgets import widget


class Button(widget.Widget):
    def __init__(self, text, onClick, font, pos, size, bevel="auto"):
        assert 0<=pos[0]<1 and 0<=pos[1]<1
        assert 0<=size[0]<=1 and 0<=size[1]<=1
        assert size[0]+pos[0]<=1 and size[1]+pos[1]<=1

        self.text = text
        self.onClick = onClick
        self.font = font
        # Pos and size are inputted as percentages, this scales them for the screen
        self.pos = scale(pos)  # pos is (x,y), assumed to be the top left
        self.size = scale(size)  # size is the dimensions of the button

        self.surface = pygame.display.get_surface()

        self.mouseOver = False # Keeps track of if the button is being moused over
        self.downClicked = False # Keeps track of whether you clicked on the button but have not yet released

        self.bevel = scaleOrDefault(bevel, diagonal(self.size)/12, [0, max(self.size[1]/2, self.size[0]/2)])

        self.box = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def rescale(self, oldSize, newSize): # for when the window is changed to a different size
        self.pos = rescaleForSizeChange(self.pos, oldSize, newSize)
        self.size = rescaleForSizeChange(self.size, oldSize, newSize)
        self.bevel = rescaleForSizeChange(self.bevel, oldSize, newSize)

    def render(self):

        if self.mouseOver:
            backgroundColor = GRAY
        else:
            backgroundColor = WHITE

        # Fills the button with the interior color, depends on whether the mouse is hovering or not
        pygame.draw.polygon(self.surface, backgroundColor,getPoly(self.pos,self.size,self.bevel))

        # Thin black outline around the button
        self.box = pygame.draw.polygon(self.surface, BLACK, getPoly(self.pos,self.size,self.bevel), 1)

        text = self.font.render(self.text, False, (0, 0, 0))

        textSize = self.font.size(self.text)
        self.surface.blit(text, (self.pos[0]+(self.size[0]-textSize[0])/2, self.pos[1]+(self.size[1]-textSize[1])/2))

class TextButton(Button): # Text you can click on

    def render(self):

        text = self.font.render(self.text, False, (0, 0, 0))

        textSize = self.font.size(self.text)
        self.box = self.surface.blit(text, (self.pos[0] + (self.size[0] - textSize[0]) / 2, self.pos[1] + (self.size[1] - textSize[1]) / 2))

class TabButton(Button):

    def __init__(self, text, onClick, tabNumber, font, pos, size, bevel="auto", isSelected=False):
        super(TabButton, self).__init__(text, onClick, font, pos, size, bevel)
        self.tabNumber = tabNumber
        self.isSelected = isSelected

    def upClick(self):
        if self.downClicked and self.isMouseOver():
            self.onClick(self.tabNumber)

        self.downClicked = False

    def render(self):

        rightX = self.pos[0] + self.size[0]
        botY = self.pos[1] + self.size[1]

        if self.isSelected:
            backgroundColor = LIGHT_GRAY
        else:
            backgroundColor = WHITE

        if self.mouseOver:
            backgroundColor = GRAY

        tabShape = [[self.pos[0] + self.bevel, self.pos[1]], [rightX - self.bevel, self.pos[1]], [rightX, self.pos[1] + self.bevel],
                    [rightX, botY], [self.pos[0], botY], [self.pos[0], self.pos[1] + self.bevel]]

        pygame.draw.polygon(self.surface, backgroundColor, tabShape)  # Fills the button with the interior color

        self.box = pygame.draw.polygon(self.surface, BLACK, tabShape, 1)  # Thin black outline around the button

        text = self.font.render(self.text, False, (0, 0, 0))

        textSize = self.font.size(self.text)
        self.surface.blit(text, (self.pos[0] + (self.size[0] - textSize[0]) / 2, self.pos[1] + (self.size[1] - textSize[1]) / 2))

# This isn't a button subclass, but I'll leave it here because it's about buttons and uses a list of them
# Should button list instead just be a function which makes a lot of buttons? It would function similarly
class ButtonList:

    def __init__(self, texts, onClicks, font, pos, size, gap, direction = "horizontal", bevel="auto"):

        self.buttons = []
        for i in range(0, len(texts)):
            if direction == "horizontal":
                self.buttons.append(Button(texts[i], onClicks[i], font, [pos[0]+(size[0]+gap)*i, pos[1]], size, bevel))
            else:
                self.buttons.append(Button(texts[i], onClicks[i], font, [pos[0], pos[1]+(size[1]+gap)*i], size, bevel))

    def checkMouseOver(self):
        for button in self.buttons:
            button.checkMouseOver()

    def downClick(self):
        for button in self.buttons:
            button.downClick()

    def upClick(self):
        for button in self.buttons:
            button.upClick()

    def rescale(self, oldSize=(1,1), newSize=(1,1)):
        for button in self.buttons:
            button.rescale(oldSize, newSize)

    def render(self):
        for button in self.buttons:
            button.render()
