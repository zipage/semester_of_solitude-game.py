def start_game():
    print(
        ">> It was pouring rain when you finally managed to bring the last of your bags in. You are relived to finally be inside."
    )
    print(">> You head in the elevator to Floor 3.")
    print(
        ">> You read 307 on the apartment door. This was your new home for the semester."
    )
    print(
        ">> You remove your face mask and hang up your soaked jacket, with your shoes at the door."
    )

    #
    #
    #
    # if they choose sleep:
    # print("*BEEP* *BEEP* *BEEP*")
    # print("Your alarm blares, piercing through the quiet solitude of your apartment.")
    # print(
    #   "*YAWN* You rub your eyes as you start to wake  up. You reach for your phone and scroll through your notifications."
    # )
    #
    #

    # starting the actual game yes or no here:


while True:

    start_game = input(
        "Are you ready to start your first semester? (yes/no)"
    ).lower()  # converts all text to lowercase
    if start_game == "yes":
        print(
            "--- You are officially living on Capital Univerities campus in a tiny bachelor apartment. --"
        )
        break
    elif start_game == "no":
        print(
            ">> You change your mind about starting the semester. You reach out to Student Service and cancel your University enrollment."
        )
        print(
            ">> You moved back Home, just in time before the boarders closed due to DIVOC-91."
        )
        print("The game is now over...")
        break
    else:
        print("* Invalid choice. Please choose 'yes' or 'no'. *")

print(
    ">> * You check your watch. It's 9:48pm * You are exhausted from moving. You head straight to bed."
)
print("*BEEP* *BEEP* *BEEP*")
print("Your alarm blares, piercing through the quiet solitude of your apartment.")
print(
    "*YAWN* You rub your eyes as you start to wake  up. You reach for your phone and scroll through your notifications."
)


print("What is your name?")
playerName = input("> ")
player = playerName

print("You login to the Capital Universities student portal.")
# Prompt to declare their Major:
print(
    ">> Congradulations on enrolling at Capital University, "
    + playerName
    + "! Please declare your Major:"
)
playerMajor = input("> ")
print(
    ">> You officially choose your Major. You are now enrolled as a freshman student in "
    + playerMajor
    + ", at Capital University!"
)
