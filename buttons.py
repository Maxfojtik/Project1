import pygame
from colors import *


class Button(object):
    def __init__(self, text, onClick, font, pos, size, bevel="auto"):
        self.text = text
        self.onClick = onClick
        self.font = font
        # Pos and size are inputted as percentages, this scales them for the screen
        screenSize = pygame.display.get_surface().get_size()
        self.pos = [pos[i]*screenSize[i] for i in range(0,2)]  # pos is (x,y), assumed to be the top left
        self.size = [size[i]*screenSize[i] for i in range(0,2)]  # size is the dimensions of the button
        self.surface = pygame.display.get_surface()

        self.mouseOver = False # Keeps track of if the button is being moused over
        self.downClicked = False # Keeps track of whether you clicked on the button but have not yet released

        if bevel == "auto":
            bevel = self.size[1]/4
        else:
            bevel *= size[0]  # Scale the bevel for the screen
        self.bevel = min(min(self.size[1]/2, self.size[0]/2), bevel)  # Makes sure that the bevel is less than the sides

        assert pos[0]<1 and pos[1]<1
        assert size[0]<1 and size[1]<1

        self.render() # Rendering initializes self.box

    def checkMouseOver(self):
        self.mouseOver = self.box.collidepoint(pygame.mouse.get_pos())
        return self.mouseOver

    def downClick(self):
        # Down click is here because buttons should only activate if you click down then up on them
        self.downClicked = self.checkMouseOver()

    def upClick(self):
        if self.downClicked and self.checkMouseOver():
            self.onClick()
        else:
            print("Hello")
        self.downClicked=False

    def rescale(self, oldSize, newSize): # for when the window is changed to a different size
        self.pos = [self.pos[i]*(newSize[i]/oldSize[i]) for i in range(0,2)]
        self.size = [self.size[i]*(newSize[i]/oldSize[i]) for i in range(0,2)]

    def render(self):

        rightX = self.pos[0]+self.size[0]
        botY = self.pos[1]+self.size[1]

        if self.mouseOver:
            backgroundColor = GRAY
        else:
            backgroundColor = WHITE

        # Fills the button with the interior color, depends on whether the mouse is hovering or not
        pygame.draw.polygon(self.surface, backgroundColor,
                            [[self.pos[0] + self.bevel, self.pos[1]], [rightX - self.bevel, self.pos[1]],
                             [rightX, self.pos[1] + self.bevel], [rightX, botY - self.bevel],
                             [rightX - self.bevel, botY], [self.pos[0] + self.bevel, botY],
                             [self.pos[0], botY - self.bevel], [self.pos[0], self.pos[1] + self.bevel]])

        # Thin black outline around the button
        self.box = pygame.draw.polygon(self.surface, BLACK, [[self.pos[0] + self.bevel, self.pos[1]], [rightX - self.bevel, self.pos[1]],
                                                  [rightX, self.pos[1]+self.bevel], [rightX, botY-self.bevel],
                                                  [rightX - self.bevel, botY], [self.pos[0] + self.bevel, botY],
                                                  [self.pos[0], botY - self.bevel], [self.pos[0], self.pos[1] + self.bevel]], 1)

        text = self.font.render(self.text, False, (0, 0, 0))

        textSize = self.font.size(self.text)
        self.surface.blit(text, (self.pos[0]+(self.size[0]-textSize[0])/2, self.pos[1]+(self.size[1]-textSize[1])/2))

class MenuButton(Button):

    def render(self):

        rightX = self.pos[0]+self.size[0]
        botY = self.pos[1]+self.size[1]

        if self.mouseOver:
            backgroundColor = GRAY
        else:
            backgroundColor = WHITE

        # Fills the button with the interior color, depends on whether the mouse is hovering or not
        pygame.draw.polygon(self.surface, backgroundColor,
                            [[self.pos[0] + self.bevel, self.pos[1]], [rightX - self.bevel, self.pos[1]],
                             [rightX, self.pos[1] + self.bevel], [rightX, botY - self.bevel],
                             [rightX - self.bevel, botY], [self.pos[0] + self.bevel, botY],
                             [self.pos[0], botY - self.bevel], [self.pos[0], self.pos[1] + self.bevel]])

        # Thin black outline around the button
        self.box = pygame.draw.polygon(self.surface, BLACK, [[self.pos[0] + self.bevel, self.pos[1]], [rightX - self.bevel, self.pos[1]],
                                                  [rightX, self.pos[1]+self.bevel], [rightX, botY-self.bevel],
                                                  [rightX - self.bevel, botY], [self.pos[0] + self.bevel, botY],
                                                  [self.pos[0], botY - self.bevel], [self.pos[0], self.pos[1] + self.bevel]], 1)

        text = self.font.render(self.text, False, (0, 0, 0))

        textSize = self.font.size(self.text)
        self.surface.blit(text, (self.pos[0]+(self.size[0]-textSize[0])/2, self.pos[1]+(self.size[1]-textSize[1])/2))

class TextButton(Button):

    def render(self):

        text = self.font.render(self.text, False, (0, 0, 0))

        textSize = self.font.size(self.text)
        self.box = self.surface.blit(text, (self.pos[0] + (self.size[0] - textSize[0]) / 2, self.pos[1] + (self.size[1] - textSize[1]) / 2))

# This needs a bit of a rework for a row of buttons before it is usable
class TabButton(Button):

    def __init__(self, text, onClick, tabNumber, font, pos, size, bevel="auto", isSelected=False):
        self.tabNumber = tabNumber
        self.isSelected = isSelected
        super(TabButton, self).__init__(text, onClick, font, pos, size, bevel)

    def upClick(self):
        if self.downClicked and self.checkMouseOver():
            self.onClick(self.tabNumber)
        else:
            print("Hello")
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

        # These do the same thing at the moment but it can be changed to give the selected tab a new box
        # if self.tabSelected:
        tabShape = [[self.pos[0] + self.bevel, self.pos[1]], [rightX - self.bevel, self.pos[1]], [rightX, self.pos[1] + self.bevel],
                    [rightX, botY], [self.pos[0], botY], [self.pos[0], self.pos[1] + self.bevel]]
        # else:
        #     tabShape = [[self.pos[0] + self.bevel, self.pos[1]], [rightX - self.bevel, self.pos[1]], [rightX, self.pos[1] + self.bevel],
        #                 [rightX, botY], [self.pos[0], botY], [self.pos[0], self.pos[1] + self.bevel]]

        # Fills the button with the interior color, depends on whether the mouse is hovering or not
        pygame.draw.polygon(self.surface, backgroundColor, tabShape)

        # Thin black outline around the button
        self.box = pygame.draw.polygon(self.surface, BLACK, tabShape, 1)

        text = self.font.render(self.text, False, (0, 0, 0))

        textSize = self.font.size(self.text)
        self.surface.blit(text, (
        self.pos[0] + (self.size[0] - textSize[0]) / 2, self.pos[1] + (self.size[1] - textSize[1]) / 2))

# This isn't a button subclass, but I'll leave it here because it's about buttons and uses a list of them
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

# class ButtonSet() # Maybe something for a list of buttons, so you can make/display a bunch together?