from screenState import *

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
fps = 60

# -------- Main Program Loop -----------
assert carryOn and screenSize
while carryOn:
    from screenState import * # Not sure why buttons only work if this line is here. why? Why? WHY? WHYYYYYY??????????
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop.

        activeScreen.checkMouseOver()

        if event.type == pygame.MOUSEBUTTONDOWN:
            activeScreen.downClick()

        elif event.type == pygame.MOUSEBUTTONUP:
            activeScreen.upClick()

        if event.type == pygame.VIDEORESIZE:
            oldSize = screenSize
            surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            screenSize = pygame.display.get_surface().get_size()
            for screen in screens.values():
                screen.rescale(oldSize, screenSize)


    # --- Game logic should go here


    # --- Drawing code below:
    # First, clear the screen to white.
    windowScreen.fill(WHITE)
    activeScreen.render()

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(fps)

# Once we have exited the main program loop we can stop the game engine:
pygame.quit()

