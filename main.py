import sys
import json
from AccountAuth import AccountAuth
from BankAccount import BankAccount
from UserInterface import UserInterface

def main():
    interface = UserInterface()
    interface.startup_page()

if __name__ == "__main__":
    main()