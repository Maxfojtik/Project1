from buttons import *
from screens import *
from tabbedSection import *
from fonts import *
from pygame.locals import *
from sliders import *
import mainMenu
import settingsMenu

# For every screen there is a dictionary entry
# These will have the information on the screen like buttons
# To switch, change the variable which has the active screen, and then you can call its render function

pygame.init()

screenSize = (1280, 720)
windowScreen = pygame.display.set_mode(screenSize, RESIZABLE)
pygame.display.set_caption("Project 1")

carryOn = True

screens = {
    "Main Menu" : Screen([
        ButtonList(["Start Game", "Join Game", "Host Game", "Settings", "Credits", "Quit"],
               [mainMenu.startGame,mainMenu.joinGame,mainMenu.hostGame,mainMenu.settings,mainMenu.gameCredits,mainMenu.quitGame],
                   someFont, [.75, .30], [.14,.07], .03, "vertical")
    ]),
    "Settings" : Screen([
        TabbedSection(["Audio","Game","Video"],
                      [[Button("Audio",settingsMenu.audio,someFont,[.42,.40],[.14,.07]),
                        Slider([.2,.2],[.3,.05],[.03,.04],[0,10],False)],
                       [Button("Game",settingsMenu.game,someFont,[.43,.40],[.14,.07])],
                       [Button("Video", settingsMenu.video, someFont, [.44, .40], [.14, .07])],
                       ], [0,.05],[1,.95],someFont,
                      allTabs=[
                          ButtonList(["Cancel","Accept"],[settingsMenu.cancel,settingsMenu.accept],someFont,[.01,.91],[.14,.07],.01)
                      ]),

    ]),
}

activeScreen = screens["Settings"]