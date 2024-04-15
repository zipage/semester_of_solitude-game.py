# GAME START HERE:

# PLAYER MOVES IN GAME BEGINS
print(
    ">> It was pouring rain when you finally managed to bring the last of your bags in. You are relived to finally be inside."
)


print(">> You head in the elevator to Floor 3.")
print(">> You read 307 on the apartment door. This was your new home for the semester.")
print(
    ">> You remove your face mask and hang up your soaked jacket, with your shoes at the door."
)
print("What is your name?")
playerName = input("")  # Stores the name of the player.

# Note on the table:
print(">> You find a note on the table. Do you want to read the note? (yes / no)")
readNoteChoice = input("> ")
if readNoteChoice == "yes":
    print(
        ">> You pick up the note and it reads: * Welcome to your new place, "
        + playerName
        + ". Here's the spare key. *"
    )

elif readNoteChoice == "no":
    print(">> You'll read that note later.")

    print(" ")
else:
    print("* Hmm, that didn't work. Choose an option. *")

# make a function(?) when player types "note" they can read this
# this works but only after this thing

readNoteChoice = input("> ")
if readNoteChoice == "note" or "read note" or "Note":
    print(
        ">> You pick up the note and it reads: * Welcome to your new place, "
        + playerName
        + ". Here's the spare key. *"
    )

else:
    print("--- I am sorry, I don't know what you mean. ---")

print(
    ">> * You check your watch. It's 9:48pm * You are exhausted from moving. You head straight to bed."
)
print("*BEEP* *BEEP* *BEEP*")
print(">> Your alarm blares, piercing through the quiet solitude of your apartment.")
print(
    ">> *YAWN* You rub your eyes as you start to wake  up. You reach for your phone and scroll through your notifications."
)

# PLAYER CHOOSES MAJOR

print(
    ">> You reach beside your bed for your LAPTOP from your backpack. You already choose your classes so its time to finalize and declare your Major."
)
print(">> You login to the Capital Universities student portal.")
print("--- You are filling out your student profile ---")

print(
    ">> Congradulations on enrolling at Capital University, "
    + str(playerName)
    + "! Please declare your Major:"
)
playerMajor = input("> ")
print(
    ">> You officially choose your Major. You are now enrolled as a freshman student in "
    + str(playerMajor)
    + ", at Capital University!"
)

print(" ")
print("--- Semester of Solitude ")
print(
    "--- This is a Choose Your Own Text Adventure where you, a newly enrollend student at Capital University "
)
print(
    "--- experiences being a freshman at university while navigating life alone in the pandemic."
)
print(
    "--- The game is simple, will you be successfully and choose the right choices? That's completely up to you. "
)
print("--- Semester of Solitude; Stubby Clown Studios - 2024 ---")
print(" ")
# GAME CONTINUES

print(
    ">> After clicking the button to declare my major, I'm hit with a rush of excitement and nerves."
)
print(
    ">> It's a big step, and I can't help but wonder what this semester will hold for me. But hey, no turning back now, right?"
)

# EXPLAIN CHOICES TO THE PLAYER
print(" ")
print(
    "--- There are choices that progress the story within your gameplay. Depending on what you choose, your player will have a different ending."
)
print(
    "--- If a choice starts with an 'Ⓜ', this is a 'Major Choice'. These have a large impact the direction of your games ending, and DON'T get to be repeated."
)
print(
    "---Any other choices are ones that can be repeated throughout the game. And have a smaller impact on your games ending."
)
print(" ")
