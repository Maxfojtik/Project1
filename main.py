from screens import screenState
import pygame
from resources.colors import *
import time

start_time = time.time()
x = 1 # displays the frame rate every x seconds
displayFPS = False # Whether or not to display the framerate
counter = 0
clock = pygame.time.Clock()  # The clock will be used to control how fast the screen updates
fps = 60

mousePressed = False

# -------- Main Program Loop -----------
assert screenState.carryOn and screenState.screenSize

while screenState.carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            screenState.carryOn = False  # Flag that we are done so we exit this loop.

        screenState.activeScreen.checkMouseOver()

        if event.type == pygame.MOUSEBUTTONDOWN:
            screenState.activeScreen.downClick()
            mousePressed = True

        elif event.type == pygame.MOUSEBUTTONUP:
            screenState.activeScreen.upClick()
            mousePressed = False

        if event.type == pygame.VIDEORESIZE:
            oldSize = screenState.screenSize
            surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            screenState.screenSize = pygame.display.get_surface().get_size()
            for screen in screenState.screens.values():
                screen.rescale(oldSize, screenState.screenSize)


    # --- Game logic should go here


    # --- Drawing code below:
    # First, clear the screen to white.
    screenState.windowScreen.fill(WHITE)

    screenState.activeScreen.render()
    pygame.display.flip()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(fps)

    counter += 1
    if (time.time() - start_time) > x:
        if displayFPS:
            print("FPS: ", counter / (time.time() - start_time))
        counter = 0
        start_time = time.time()

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

