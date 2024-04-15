# Player starts with 0 knowledge and need at least 60/100 knowlege to pass thier classes


class Player:
    def __init__(self, name):
        self.name = name
        self.energy = 100  # Player's energy level
        self.knowledge = 0  # Player's knowledge level

    def study(self):
        if self.energy >= 20:
            self.energy -= 20
            self.knowledge += 10
            print("You spend some time studying. Your knowledge increases.")
        else:
            print("You're too tired to study right now. Get some rest!")

    def rest(self):
        self.energy += 30
        print("You take some time to rest and recharge.")


# Example usage:
player_name = input("Enter your name: ")
player = Player(player_name)

while True:
    print("\nWhat would you like to do?")
    print("1. Study")
    print("2. Rest")
    print("3. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        player.study()
        if player.knowledge >= 60:
            print("Congratulations! You have passed the class.")
            break
    elif choice == "2":
        player.rest()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
