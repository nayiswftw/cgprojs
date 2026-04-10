from check_balance import check_balance
from withdraw import withdraw_money
from deposit import deposit_money

balance = 1000
transactions = []

print("Welcome to SimpleBank ATM!")
print("Your current balance: $" + str(balance))
print()

while True:
    print("What do you want to do?")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    print()
    
    choice = input("Enter your choice (1-4): ")
    print()
    
    if choice == "1":
        balance = check_balance(balance)
    
    elif choice == "2":
        balance = withdraw_money(balance, transactions)
    
    elif choice == "3":
        balance = deposit_money(balance, transactions)
    
    elif choice == "4":
        print("Thank you for using SimpleBank ATM!")
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4")
        print()
