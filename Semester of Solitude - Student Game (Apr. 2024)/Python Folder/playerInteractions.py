class Player:
    def __init__(self, name):
        self.name = name
        self.energy = 100  # energy: 0 you pass out and start the next day at your bed
        self.knowledge = 0  # smarts: they need to study to increase knowledge

    def study(self):
        if self.energy >= 20:
            self.energy -= 20
            self.knowledge += 5
            print("--- You had a focused study sesh. Your KNOWLEDGE increases (+5) ---")
        else:
            print("*You're just too tired to study.* ")
            print("*YAWN* I need to head to bed soon before I passout")

    def sleep(self):
        self.energy += 30
        print(
            "--- You take a much needed rest to help you recharge. You ENERGY increases (+30) ---"
        )

playerName = input("Your name: ")
player = Player(playerName)

while True:
    print("\nWhat should I do today?")
    print("* Type the corresponding number or type the option of your choice *")
    print("1. Study")
    print("2. Go to sleep")
    print("3. Quit")

    choice = input("What shall I do?")

    if choice == "1" or "Study" or "study":
        player.study()
        if player.knowledge >= 60:
            print("You get an popsitive email from your class administrator. Keep maintaining this grade to pass your course.")
            break
        elif choice == "2" or "Sleep" or "sleep" or "Go to sleep" or "go to sleep":
            player.rest()
        elif choice == "3" or "Quit" or "quit" or "end game":



            #################################3

                # the Players information:
    #    class Player:
    #        def __init__(self, name):
    #            self.name = name
    #            self.energy = 55  # Players energy levels
    #            self.knowledge = 0  # Players knowledge levels
    #            self.hunger = 25  # Start day on 25/100 hunger level
    #            self.socialEnergy = 50  # starts game at 50/50


########################
view note:
def viewNote():
    viewNote = input("view note" or "note")
    if viewNote == "view note" or viewNote == "note":
        print(
            ">> You pick up the note and it reads: Welcome to your new place, "
            + playerName
            + ". Here's the spare key."
        )
    else:
        print("Sorry, I don't know what you mean.")
