from buttons import TabButton
from colors import *
from screenScaling import *

class TabbedSection:

    def __init__(self, tabNames, tabsContent, pos, size, font, buttonSize="auto", bevel="auto"):
        if buttonSize=="auto":
            buttonSize=(.14,.07)

        self.tabSelected = 0;
        self.buttons = []
        self.tabsContent = tabsContent
        self.tabNames = tabNames
        # Pos and size are inputted as percentages, this scales them for the screen
        self.pos = scale(pos)  # pos is (x,y), assumed to be the top left
        self.size = scale(size)  # size is the dimensions of the tabbed section
        self.buttonSize = scale(buttonSize)  # The dimensions of the tab buttons
        self.surface = pygame.display.get_surface()

        if bevel == "auto":
            bevel = self.size[1]/4
        else:
            self.bevel *= size[0]  # Scale the bevel for the screen
        self.bevel = min(min(self.size[1]/2, self.size[0]/2), bevel)  # Makes sure that the bevel is less than the sides

        for i in range(0,len(tabNames)):
            self.buttons.append(TabButton(tabNames[i], self.focus, font, [pos[0]+buttonSize[0]*i, pos[1]], buttonSize, bevel))


    def focus(self): # This may need to be converted to a TabButton function
        pass

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
        pass

    def render(self):

        # Draw background for buttons:
        self.surface.fill(DARK_BLUE, [self.pos[0],self.pos[1],self.size[0],self.size[1]])
        pygame.draw.rect(self.surface, BLACK, [self.pos[0],self.pos[1],self.size[0],self.size[1]], 1)

        # Draw background for section below tabs
        self.surface.fill(BLUE, [self.pos[0], self.pos[1]+self.buttonSize[1], self.size[0], self.size[1]-self.buttonSize[1]])
        pygame.draw.rect(self.surface, BLACK, [self.pos[0], self.pos[1]+self.buttonSize[1], self.size[0], self.size[1]-self.buttonSize[1]], 1)

        for button in self.buttons:
            if not button.tabSelected:
                button.render()
        for button in self.buttons:
            if button.tabSelected:
                button.render()
