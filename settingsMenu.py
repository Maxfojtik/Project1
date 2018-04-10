import screenSwitch

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
    screenSwitch.switchScreen("Main Menu")
    print("Cancel")

def accept():
    screenSwitch.switchScreen("Main Menu")
    print("Accept")