import pygame
from pygame.locals import *
screenSize = (700, 500)
from buttons import Button
from colors import *

pygame.init()  # Open a new window
pygame.font.init()

# Define some colors


someFont = pygame.font.SysFont('Times New Roman', 15)

screen = pygame.display.set_mode(screenSize, RESIZABLE)
pygame.display.set_caption("Project 1")

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
fps = 60

buttons = [
    Button("Join Game", someFont, [.70, .45], [.14, .07], screen, "auto"),
    Button("Host Game", someFont, [.70, .54], [.14, .07], screen, "auto")
]

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop.

        for button in buttons:
            button.checkMouseOver()

        if event.type == pygame.MOUSEBUTTONDOWN:
            # When clicks become a file, things below this will just be part of a function call to it
            for button in buttons:
                button.downClick()

        elif event.type == pygame.MOUSEBUTTONUP:
            # When clicks become a file, things below this will just be part of a function call to it
            for button in buttons:
                button.upClick()

        if event.type == pygame.VIDEORESIZE:
            oldSize = screenSize
            surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            screenSize = pygame.display.get_surface().get_size()
            for button in buttons:
                button.rescale(oldSize, screenSize)


    # --- Game logic should go here


    # --- Drawing code below:
    # First, clear the screen to white.
    screen.fill(WHITE)

    for button in buttons:
        button.render()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(fps)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
