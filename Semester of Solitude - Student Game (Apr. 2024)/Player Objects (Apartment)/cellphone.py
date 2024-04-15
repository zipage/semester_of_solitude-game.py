# EXAMPLE CODE:


class Cellphone:
    def __init__(self):
        self.battery_life = 100  # Initial battery life
        self.messages = []
        self.emails = []

    def charge_battery(self, amount):
        self.battery_life = min(
            100, self.battery_life + amount
        )  # Ensure battery life doesn't exceed 100

    def receive_message(self, sender, message):
        self.messages.append((sender, message))

    def check_messages(self):
        for sender, message in self.messages:
            print(f"Message from {sender}: {message}")

    def receive_email(self, sender, subject, content):
        self.emails.append((sender, subject, content))

    def check_emails(self):
        for sender, subject, content in self.emails:
            print(f"Email from {sender} - Subject: {subject}\n{content}")


# simulate interactions:

# Create a cellphone object
my_phone = Cellphone()

# Simulate receiving a message
my_phone.receive_message("Friend", "Hey, want to hang out later?")

# Simulate receiving an email
my_phone.receive_email(
    "Professor",
    "Assignment Reminder",
    "Don't forget to submit your assignment by Friday.",
)

# Check messages and emails
my_phone.check_messages()
my_phone.check_emails()
