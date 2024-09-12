import json

class DatabaseController:
    def __init__(self, filename):
        self.filename = filename

    def read_database(self):    
        with open(self.filename, 'r') as data:
            return json.load(data)
        
    def write_user_to_database(self, newData):
        with open(self.filename, 'w') as data:
            json.dump(newData, data, indent=4)
    
    def check_username_availablility(self, username):
        data = self.read_database()
        for user in data["users"]:
            if user["username"] == username:
                return False
        return True

    def get_checkings_from_database(self, username):
        data = self.read_database()
        for user in data["users"]:
            if user["username"] == username:
                return user["checkings"]
        print("Username Not Found")

    def get_savings_from_database(self, username):
        data = self.read_database()
        for user in data["users"]:
            if user["username"] == username:
                return user["savings"]
        print("Username Not Found")
        
    def create_database_account(self, username, password, checkings = 0.0, savings = 0.0):
        data = self.read_database()
        for user in data["users"]:
            if user["username"] == username:
                print("\nUsername Already Exists, Try Again")
                return False
        newUser = {
            "username": username,
            "password": password,
            "checkings": checkings,
            "savings": savings
        }
        data["users"].append(newUser)
        self.write_user_to_database(data)
        print("Created New Account Successfully")
        return True

    def read_database_account(self, username):
        data = self.read_database()
        for user in data["users"]:
            if user["username"] == username:
                return user
        print("Account Not Found")
        return None

    def update_database_account(self, username, password = None, checkings = None, savings = None):
        data = self.read_database()
        foundUser = False

        for user in data["users"]:
            if user["username"] == username:
                user_found = True
                if password is not None:
                    user["password"] = password
                if checkings is not None:
                    user["checkings"] = checkings
                if savings is not None:
                    user["savings"] = savings
                self.write_user_to_database(data)
                foundUser = True
                print("Updated Successfully")
                break
        if foundUser == False:
            print("Username Not Found")