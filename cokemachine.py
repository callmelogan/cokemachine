due = 50
cents = int(input("Enter your money: "))

while cents != due:
    if cents != 25 or cents != 15 or cents != 5:
        cents = int(input("Enter your money again: "))
        cents = cents + cents
    
    else:
        due = due - cents
        print(due)
