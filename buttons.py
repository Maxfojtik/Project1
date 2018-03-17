import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)


class Button(object):
    def __init__(self, text, font, pos, size, surface, bevel=0):
        self.text = text
        self.font = font
        self.pos = pos  # pos is (x,y), assumed to be the top left
        self.size = size  # size is the dimensions of the button, assumed to be (x,y)
        self.surface = surface  # The screen that the button is on
        self.mouseOver = False

        if bevel == "auto":
            bevel = self.size[1]/4
        self.bevel = min(min(self.size[1]/2, self.size[0]/2), bevel)  # Makes sure that the bevel is less than the sides
        self.render()

    def checkMouseOver(self):
        self.mouseOver = self.box.collidepoint(pygame.mouse.get_pos())

    def render(self):
        rightX = self.pos[0]+self.size[0]
        botY = self.pos[1]+self.size[1]

        if self.mouseOver:
            backgroundColor = GRAY
        else:
            backgroundColor = WHITE

        pygame.draw.polygon(self.surface, backgroundColor,
                            [[self.pos[0] + self.bevel, self.pos[1]], [rightX - self.bevel, self.pos[1]],
                             [rightX, self.pos[1] + self.bevel], [rightX, botY - self.bevel],
                             [rightX - self.bevel, botY], [self.pos[0] + self.bevel, botY],
                             [self.pos[0], botY - self.bevel], [self.pos[0], self.pos[1] + self.bevel]])

        # Outline. This is a thin black line around the button
        self.box=pygame.draw.polygon(self.surface, BLACK, [[self.pos[0] + self.bevel, self.pos[1]], [rightX - self.bevel, self.pos[1]],
                                                  [rightX, self.pos[1]+self.bevel], [rightX, botY-self.bevel],
                                                  [rightX - self.bevel, botY], [self.pos[0] + self.bevel, botY],
                                                  [self.pos[0], botY - self.bevel], [self.pos[0], self.pos[1] + self.bevel]], 1)
        text = self.font.render(self.text, False, (0, 0, 0))

        textSize = self.font.size(self.text)
        self.surface.blit(text, (self.pos[0]+(self.size[0]-textSize[0])/2, self.pos[1]+(self.size[1]-textSize[1])/2))



