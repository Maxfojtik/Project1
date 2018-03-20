import sys

def startGame():
    print("Start Game")

def joinGame():
    print("Join Game")

def hostGame():
    print("Host Game")

def settings():
    main.activeScreen = main.screens["Settings"]
    print("Settings")

def gameCredits():
    print("Credits")

def quitGame():
    sys.exit()

import main