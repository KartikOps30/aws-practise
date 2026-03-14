# -*- coding: utf-8 -*-

balance = 0

def deposit(amount):
    global balance
    balance += amount
    print("Deposited Rs." + str(amount) + " Current Balance: Rs." + str(balance))

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance -= amount
        print("Withdrew Rs." + str(amount) + " Current Balance: Rs." + str(balance))

def check_balance():
    print("Your Balance is: Rs." + str(balance))

deposit(5000)
deposit(2000)
withdraw(1500)
withdraw(10000)
check_balance()