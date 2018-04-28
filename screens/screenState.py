from screenComponents.widgets.buttons import *
from screenComponents.widgets.switches import *
from screenComponents.containers.tabbedSection import *
from resources.fonts import *
from pygame.locals import *
from screenComponents.widgets.sliders import *
from screens import mainMenu, settingsMenu
from defines.debug import *
from screenComponents.containers.scrollView import *


def switchScreen(switchTo, backward=False): # Switch between screens
    global activeScreen
    activeScreen = screens[switchTo]
    if not backward:
        prevScreens.append(switchTo)
        if PRINT_SCREEN_SWITCHING:
            print("Forward to:",switchTo,"New array:",prevScreens)
    return activeScreen

def back(): # Go back to the previous screen
    goal = prevScreens[0]
    prevScreens.pop()
    if PRINT_SCREEN_SWITCHING:
        print ("Backward to:",goal,end=" ")
    switchScreen(goal, True)
    if PRINT_SCREEN_SWITCHING:
        print("New array:",prevScreens)


# For every screen there is a dictionary entry
# These will have the information on the screen like buttons
# To switch, change the variable which has the active screen, and then you can call its render function

pygame.init()

screenSize = (1280, 720)
windowScreen = pygame.display.set_mode(screenSize, RESIZABLE)
pygame.display.set_caption("Project 1")

carryOn = True

prevScreens = [] # The names (keys) of previous screens, with the top entry being the current screen


screens = {
    "Main Menu" : Screen([
        ScrollView(
            [
                Button("hello", print, someFont, (.2,.3),(.14,.07))
            ], (.15,.25), (.1,.1)
        ),
        ButtonList(["Start Game", "Join Game", "Host Game", "Settings", "Credits", "Quit"],
                   [mainMenu.startGame, mainMenu.joinGame, mainMenu.hostGame, mainMenu.settings, mainMenu.gameCredits, mainMenu.quitGame],
                   someFont, [.75, .30], [.14,.07], .03, "vertical")
    ]),
    "Settings" : Screen([
        TabbedSection(["Audio","Game","Video"],
                      [[
                          Button("Audio", settingsMenu.audio, someFont, [.42, .40], [.14, .07]),
                          Slider([.2,.2],[.3,.05],.05,print),
                          Switch([.2,.4],[.10,.06])
                      ],
                       [Button("Game", settingsMenu.game, someFont, [.43, .40], [.14, .07])],
                       [Button("Video", settingsMenu.video, someFont, [.44, .40], [.14, .07])],
                       ], [0,.05],[1,.95],someFont,
                      allTabs=[
                          ButtonList(["Cancel","Accept"], [settingsMenu.cancel, settingsMenu.accept], someFont, [.01, .91], [.14, .07], .01)
                      ]),

    ]),
}

activeScreen = switchScreen("Main Menu")


