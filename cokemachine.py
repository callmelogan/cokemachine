# due = 50
# cents = int(input("Enter your money: "))

# while cents != due:
#     if cents != 25 or cents != 15 or cents != 5:
#         cents = int(input("Enter your money again: "))
#         cents = cents + cents
    
#     else:
#         due = due - cents
#         print(due)
coke = 50
print("Amount Due: ",+coke)
while(coke>0):
    coin = int(input("Insert Coin: "))
    if coin == 10:
        coke=coke-coin
    elif coin == 25:
        coke=coke-coin
    elif coin == 5:
        coke=coke-coin
    print("Amount Due: ",+coke)
