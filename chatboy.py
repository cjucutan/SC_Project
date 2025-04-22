"""
Description: Chatbot application.  Allows user to perform 
balance inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: {Student Name}
Date: 2023-10-15
Usage: From the console: python src/chatbot.py
"""

import os

ACCOUNTS = {
    123456: {"balance": 1000.0},
    789012: {"balance": 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

def get_account() -> int:
    user_input = int(input("Please Enter your Account Number:"))
    if user_input not in ACCOUNTS:
        raise ValueError("Account Number Does not Exist.")
    return user_input

def get_amount() -> float:
    user_input_1 = float(input("Enter the transaction amount:"))
    if user_input_1 <= 0:
        raise ValueError("Invalid amount. Please enter a positive number.")
    return user_input_1

def get_balance(account: int) -> str:
    balance = ACCOUNTS[account]["balance"]
    return f"Your current balance for account {account} is ${balance:.2f}"

def make_deposit(account: int, amount: float) -> str:
    ACCOUNTS[account]["balance"] += amount
    return f"You have made a deposit of ${amount:.2f} to account {account}"

def user_selection() -> str:
    user_input_two = input("What would you like to do (balance/deposit/exit)?").lower()
    if user_input_two not in VALID_TASKS:
        raise ValueError("Invalid task. Please choose balance, deposit, or exit.")
    return user_input_two

def chatbot():
    print("Welcome! I'm the PiXELL River Financial Chatbot! Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            selection = user_selection()

            if selection != "exit":
                valid_account = False
                while not valid_account:
                    try:
                        account = get_account()
                        valid_account = True
                    except ValueError as e:
                        print(e)

                if selection == "balance":
                    balance = get_balance(account)
                    print(balance)
                else:
                    valid_amount = False
                    while not valid_amount:
                        try:
                            amount = get_amount()
                            valid_amount = True
                        except ValueError as e:
                            print(e)
                    print(make_deposit(account, amount))
            else:
                keep_going = False
        except ValueError as e:
            print(e)

    # Logging to file (exposing potentially sensitive information)
    with open("log.txt", "a") as f:
        f.write("Chatbot session ended by user.\n")

    # Unsanitized system call (could lead to code injection)
    os.system(f"echo Goodbye, $USER")

    print("Thank you for banking with PiXELL River Financial.")

if __name__ == "__main__":
    chatbot()

