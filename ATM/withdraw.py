def withdraw_money(balance, transactions):
    amount = int(input("How much money do you want to withdraw? $"))
    
    if amount > balance:
        print("You don't have enough money!")
        print()
    elif amount <= 0:
        print("Amount must be greater than 0!")
        print()
    else:
        balance = balance - amount
        transactions.append(["withdraw", amount])
        print("You withdrew: $" + str(amount))
        print("New balance: $" + str(balance))
        print()
    
    return balance
