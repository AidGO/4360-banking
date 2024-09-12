import sys
from AccountAuth import AccountAuth
from BankAccount import BankAccount

class UserInterface:
    def __init__(self):
        self.auth = AccountAuth()
        self.account = None

    def startup_page(self):
        options = ["1", "2", "3"]
        while True:
            print("\nOptions:\nLogin (1)\nCreate Account(2)\nExit (3)")
            option = input("\nChoose an Option:")
            if option not in options:
                print("\nInvalid Option")
            else:
                if option == "1":
                    self.login_page()
                    break

                elif option == "2":
                    self.create_account_page()
                    break

                elif option == "3":
                    break
                    sys.exit()


    def login_page(self):
        options = ["1", "2"]
        while True:
            print("\nOptions:\nLogin (1)\nExit (2)")
            option = input("\nChoose an Option:")
            if option not in options:
                print("\nInvalid Option")
            else:
                if option == "1":
                    if self.auth.check_attempts() == False:
                        print("\nToo Many Login Attempts, Try Again Later")
                    else:
                        print("\nAccount Login:")
                        username = input("Enter Username: ")
                        password = input("Enter Password: ")
                        if self.auth.login(username, password) == True:
                            self.account = BankAccount(username)
                            self.account_page()
                            break

                elif option == "2":
                    break
                    sys.exit()


    def create_account_page(self):
        while True:
            print("\nCreate Account:")
            username = input("Enter Username: ")
            password = input("Enter Password: ")
            if self.auth.create_account(username, password) == True:
                self.login_page()
                break

    def account_page(self):
        options = ["1", "2", "3", "4", "5", "6"]
        while True:
            self.account.print_account_balance()
            print("\nOptions:\nDeposit (1)\nWithdraw (2)\nTransfer Checkings To Savings: (3)\nTransfer Savings To Checkings: (4)\nChange Password: (5)\nExit: (6)")
            option = input("\nChoose an Option:")
            if option not in options:
                print("\nInvalid Option")
            else:
                if option == "1":
                    amount = input("\nEnter Amount to Deposit: ")
                    self.account.deposit(amount)

                elif option == "2":
                    amount = input("\nEnter Amount to Withdraw: ")
                    self.account.withdraw(amount)

                elif option == "3":
                    amount = input("\nEnter Transfer Amount (Checkings -> Savings): ")
                    self.account.transfer_checkings_to_savings(amount)
                
                elif option == "4":
                    amount = input("\nEnter Transfer Amount (Savings -> Checkings): ")
                    self.account.transfer_savings_to_checkings(amount)

                elif option == "5":
                    newPassword = input("\nEnter New Password: ")
                    self.account.set_account_password(newPassword)

                elif option == "6":
                    break
                    sys.exit()