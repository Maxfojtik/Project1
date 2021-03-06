from screenComponents.widgets.buttons import TabButton
from resources.colors import *
from resources.screenTools import *
from screenComponents.containers.screen import Screen

class TabbedSection(Screen):

    def __init__(self, tabNames, tabsContent, pos, size, font, buttonSize="auto", bevel="auto", allTabs=None):
        Screen.__init__(self, tabsContent, pos, size)
        self.tabSelected = 0
        self.tabButtons = []
        self.tabsContent = tabsContent
        if allTabs: # If you have some allTab content
            self.allTabs = allTabs
        else:
            self.allTabs = []
        self.tabNames = tabNames
        self.buttonSize = scaleOrDefault(buttonSize, scale((.14, .07)))
        self.surface = pygame.display.get_surface()

        buttonSize = scaleOrDefault(buttonSize, [.14, .07])
        bevel = scaleOrDefault(bevel, "auto", [min(buttonSize[0] / 2, buttonSize[1] / 2), min(buttonSize[1], buttonSize[0])])

        for i in range(0,len(tabNames)):
            self.tabButtons.append(TabButton(tabNames[i], self.focus, i, font, [pos[0]+buttonSize[0]*i, pos[1]], buttonSize, bevel))
        self.tabButtons[0].isSelected = True # Select the first one

    def focus(self, tabNumber):
        self.tabSelected = tabNumber
        for button in self.tabButtons:
            button.isSelected = False
        self.tabButtons[tabNumber].isSelected = True

    def checkMouseOver(self):
        for button in self.tabButtons:
            button.checkMouseOver()
        for thing in self.tabsContent[self.tabSelected]:
            thing.checkMouseOver()
        for thing in self.allTabs:
            thing.checkMouseOver()

    def downClick(self):
        for button in self.tabButtons:
            button.downClick()
        for thing in self.tabsContent[self.tabSelected]:
            thing.downClick()
        for thing in self.allTabs:
            thing.downClick()

    # Checks the upclick for all the things in the tabButtons and the current tab
    def upClick(self):
        for button in self.tabButtons:
            button.upClick()
        for thing in self.tabsContent[self.tabSelected]:
            thing.upClick()
        for thing in self.allTabs:
            thing.upClick()

    def rescale(self, oldSize, newSize):
        for button in self.tabButtons:
            button.rescale(oldSize, newSize)
        for thing in self.tabsContent[self.tabSelected]:
            thing.rescale(oldSize, newSize)
        for thing in self.allTabs:
            thing.rescale(oldSize, newSize)

        self.buttonSize = rescaleForSizeChange(self.buttonSize, oldSize, newSize)

        self.size = rescaleForSizeChange(self.size, oldSize, newSize)
        self.pos = rescaleForSizeChange(self.pos, oldSize, newSize)

    def render(self):

        # Draw background for buttons:
        self.surface.fill(DARK_BLUE, [self.pos[0],self.pos[1],self.size[0],self.size[1]])
        pygame.draw.rect(self.surface, BLACK, [self.pos[0],self.pos[1],self.size[0],self.size[1]], 1)

        # Draw background for section below tabs
        self.surface.fill(BLUE, [self.pos[0], self.pos[1]+self.buttonSize[1], self.size[0], self.size[1]-self.buttonSize[1]])
        pygame.draw.rect(self.surface, BLACK, [self.pos[0], self.pos[1]+self.buttonSize[1], self.size[0], self.size[1]-self.buttonSize[1]], 1)

        # Renders all the buttons, starting with the non-selected buttons, so that the selected button can be rendered slightly on top if wanted
        for button in self.tabButtons:
            if not button.isSelected:
                button.render()
        for button in self.tabButtons:
            if button.isSelected:
                button.render()

        # Render the content of the tab
        for thing in self.tabsContent[self.tabSelected]:
            thing.render()

        # Render the content which is for all tabs
        for thing in self.allTabs:
            thing.render()

        pygame.display.update([self.pos[0], self.pos[1], self.size[0], self.size[1]])