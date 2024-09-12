from DatabaseController import DatabaseController

class BankAccount:
    def __init__(self, accountName):
        self.db = DatabaseController("info.json")
        self.accountName = accountName
        self.savings = self.db.get_savings_from_database(accountName)
        self.checkings = self.db.get_checkings_from_database(accountName)

    def get_savings(self):
        return self.savings
    
    def get_checkings(self):
        return self.checkings
    
    def get_account_name(self):
        return self.accountName
    
    def set_savings(self, amount):
        self.savings = amount
        self.db.update_database_account(self.accountName, None, None, amount)

    def set_checkings(self, amount):
        self.checkings = amount
        self.db.update_database_account(self.accountName, None, amount, None)

    def set_account_password(self, password):
        self.db.update_database_account(self.accountName, password, None, None)

    def print_account_balance(self):
        print("_______________________" + "\n" + "Account Name: " + self.get_account_name() + "\n" + "Checkings: " + str(self.get_checkings()) + "\n" + "Savings: " + str(self.get_savings()) + "\n" + "_______________________")

    def transfer_checkings_to_savings(self, amount):
        savings = self.get_savings()
        checkings = self.get_checkings()

        if amount > checkings:
            print("Error: Insufficient Checking Funds")
        else:
            self.set_savings(savings + amount)
            self.set_checkings(checkings - amount)
    
    def transfer_savings_to_checkings(self, amount):
        savings = self.get_savings()
        checkings = self.get_checkings()

        if amount > savings:
            print("Error: Insufficient Savings Funds")
        else:
            self.set_savings(savings - amount)
            self.set_checkings(checkings + amount)
    
    def withdraw(self, amount):
        checkings = self.get_checkings()

        if amount > checkings:
            print("Error: Insufficient Checkings Funds")
        else:
            self.set_checkings(checkings - amount)
            print("Withdraw Successful")
    
    def deposit(self, amount):
        checkings = self.get_checkings()
        self.set_checkings(checkings + amount)
        print("Deposit Successful")

if __name__ == "__main__":
    Account = BankAccount("Harry D Oswald")
    Account.print_account_balance()
    Account.set_account_password("blueberry")
    Account.print_account_balance()