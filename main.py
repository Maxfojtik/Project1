import pygame
from buttons import Button
from pygame.locals import *

pygame.init()  # Open a new window
pygame.font.init()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = (700, 500)

someFont = pygame.font.SysFont('Times New Roman', 15)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("hello")

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
fps = 60

button1 = Button("test", someFont, [50, 50], [60, 30], screen, "auto")

# -------- Main Program Loop -----------
while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop. # Any reason not to just exit now?


        button1.checkMouseOver()

    # --- Game logic should go here


    # --- Drawing code below:
    # First, clear the screen to white.
    screen.fill(WHITE)

    button1.render()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(fps)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()
