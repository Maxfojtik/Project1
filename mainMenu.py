import screenState

def startGame():
    print("Start Game")

def joinGame():
    print("Join Game")

def hostGame():
    print("Host Game")

def settings():
    screenState.activeScreen = screenState.screens["Settings"]
    print("Settings")

def gameCredits():
    print("Credits")

def quitGame():
    screenState.carryOn = False
    print("Quit")


