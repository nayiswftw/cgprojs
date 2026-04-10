def deposit_money(balance, transactions):
    amount = int(input("How much money do you want to deposit? $"))
    
    if amount <= 0:
        print("Amount must be greater than 0!")
        print()
    else:
        balance = balance + amount
        transactions.append(["deposit", amount])
        print("You deposited: $" + str(amount))
        print("New balance: $" + str(balance))
        print()
    
    return balance
