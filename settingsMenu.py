import screenState

# ~~~~~~~~~~~~~~~~  Audio  ~~~~~~~~~~~~~~~~

def audio():
    print("Audio")

# ~~~~~~~~~~~~~~~~  Game  ~~~~~~~~~~~~~~~~

def game():
    print("Game")

# ~~~~~~~~~~~~~~~~  Video  ~~~~~~~~~~~~~~~~

def video():
    print("Video")


# ~~~~~~~~~~~~~~~~  General  ~~~~~~~~~~~~~~~~

def cancel():
    screenState.activeScreen = screenState.screens["Main Menu"]
    print("Cancel")

def accept():
    screenState.activeScreen = screenState.screens["Main Menu"]
    print("Accept")