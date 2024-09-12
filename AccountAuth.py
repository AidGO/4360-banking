from DatabaseController import DatabaseController

class AccountAuth():
    def __init__(self):
        self.db = DatabaseController("info.json")
        self.attemptsLeft = 3

    def check_attempts(self):
        if self.attemptsLeft == 0:
            return False
        else:
            return True

    def login(self, username, password):
        data = self.db.read_database()
        for user in data["users"]:
            if user["username"] == username and user["password"] == password:
                print("\nLogin Successful")
                return True
        else:
            self.attemptsLeft -= 1
            print("\nLogin Failed " + str(self.attemptsLeft) + " Remaining")
            return False
        
    def create_account(self, newUsername, newPassword):
        return self.db.create_database_account(newUsername, newPassword)