from pygame.locals import *
screenSize = (1000, 600)
from buttons import *
from screens import *
from tabbedSection import *
from colors import *
import mainMenu

pygame.init()
pygame.font.init()

someFont = pygame.font.SysFont('Times New Roman', 15)

windowScreen = pygame.display.set_mode(screenSize, RESIZABLE)
pygame.display.set_caption("Project 1")

# The loop will carry on until the user exit the game (e.g. clicks the close button).
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
fps = 60

def onClickForStart():
    print("On Click")

# For every screen there is a class
# These classes will have the information on the screen like buttons
# To switch, change the variable which has the active screen, and then you can call its render function

screens = {
    "Main Menu" : Screen([
        ButtonList(["Start Game", "Join Game", "Host Game", "Settings", "Credits", "Quit"],
               [mainMenu.startGame,mainMenu.joinGame,mainMenu.hostGame,mainMenu.settings,mainMenu.gameCredits,mainMenu.quitGame],
               someFont, [.75, .30], [.14,.07], .03, "vertical")
    ]),
    "Settings" : Screen([
        TabbedSection(["Audio","Game","Video"],[0,0,0],[.1,.1],[.6,.5],someFont)
    ]),
}

activeScreen = screens["Main Menu"]

# -------- Main Program Loop -----------
while carryOn:
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

