from DatabaseController import DatabaseController

class AccountAuth():
    def __init__(self):
        self.db = DatabaseController("info.json")

    def login(self, username, password):
        data = self.db.read_database()
        for user in data["users"]:
            if user["username"] == username and user["password"] == password:
                print("Login Successful")
                return True
        else:
            print("Login Failed")
            return False