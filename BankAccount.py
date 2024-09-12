from DatabaseController import DatabaseController

class BankAccount:
    def __init__(self, accountName):
        self.db = DatabaseController("info.json")
        self.accountName = accountName
        self.savings = self.db.get_savings_from_database(accountName)
        self.checkings = self.db.get_checkings_from_database(accountName)
        self.transferAttempts = 0

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
        try:
            amount = float(amount)

            if float(amount) > float(checkings) or float(amount) < 0:
                print("Error: Insufficient Checking Funds or Invalid Transfer Amount")
            else:
                self.set_savings(float(savings) + float(amount))
                self.set_checkings(float(checkings) - float(amount))
        except ValueError:
            print("Invalid Input, Please Enter a Numerical Value")
    
    def transfer_savings_to_checkings(self, amount):
        savings = self.get_savings()
        checkings = self.get_checkings()
        try:
            amount = float(amount)

            if float(amount) > float(savings) or float(amount) < 0:
                print("Error: Insufficient Savings Funds or Invalid Transfer Amount")
            else:
                self.set_savings(float(savings) - float(amount))
                self.set_checkings(float(checkings) + float(amount))
        except ValueError:
            print("Invalid Input, Please Enter a Numerical Value")
    
    def withdraw(self, amount):
        try:
            amount = float(amount)
            if float(amount) > 2000 or float(amount) < 0:
                print("Cannot Withdraw More Than $2000 or Invalid Amount")
                self.transferAttempts += 1
                print("Remaining Transfer Attempts: " + str(3 - self.transferAttempts))
            elif self.transferAttempts == 3:
                print("Too Many Transfer Attempts, Try Again Later")
            else:
                checkings = self.get_checkings()

                if float(amount) > float(checkings):
                    print("Error: Insufficient Checkings Funds")
                else:
                    self.set_checkings(float(checkings) - float(amount))
                    print("Withdraw Successful")
        except ValueError:
            print("Invalid Input, Please Enter a Numerical Value")
    
    def deposit(self, amount):
        try:
            amount = float(amount)
            if float(amount) > 2000 or float(amount) < 0:
                print("Cannot Deposit More Than $2000 or Invalid Amount")
                self.transferAttempts += 1
                print("Remaining Transfer Attempts: " + str(3 - self.transferAttempts))
            elif self.transferAttempts == 3:
                print("Too Many Transfer Attempts, Try Again Later")
            else:
                checkings = self.get_checkings()
                self.set_checkings(float(checkings) + float(amount))
                print("Deposit Successful")
        except ValueError:
            print("Invalid Input, Please Enter a Numerical Value")

if __name__ == "__main__":
    Account = BankAccount("Harry D Oswald")
    Account.print_account_balance()
    Account.set_account_password("blueberry")
    Account.print_account_balance()