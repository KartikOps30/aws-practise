import os

BALANCE_FILE = "balance.txt"
 

def get_balance():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, "r") as f:
            content = f.read()
            if content == "":
                return 0
            return int(content)
    return 0
    
def save_balance(balance):
    with open(BALANCE_FILE, "w") as f:
        f.write(str(balance))
      

print("Welcome customer")

def Deposit(amount):
    balance = get_balance()
    balance+= amount
    save_balance(balance)
    print(f"Deposited:₹{amount}.Current balance:₹{balance}")
    
def Withdraw(amount):
    balance = get_balance()
    if amount > balance:
        print("Insufficient balance!")
    else:
        balance-= amount
        save_balance(balance)
        print(f"Withdrawed :₹{amount}. Current balance:₹{balance}")
        
def Check_Balance():
    balance = get_balance()
    print(f"Your Balance is :₹{balance}")       
    
while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        d = int(input("Enter deposit amount: "))
        Deposit(d)
    elif choice == "2":
        w = int(input("Enter withdrawal amount: "))
        Withdraw(w)
    elif choice == "3":
        Check_Balance()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice!")