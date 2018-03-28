
def startGame():
    print("Start Game")

def joinGame():
    print("Join Game")

def hostGame():
    print("Host Game")

def settings():
    import main # Unfortunately, this needs to be here
    main.activeScreen = main.screens["Settings"]
    print("Settings")

def gameCredits():
    print("Credits")

def quitGame():
    import main
    main.carryOn = False


