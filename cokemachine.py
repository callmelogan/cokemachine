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
while(coke>0): #will continue to loop until value of coke is less than or equal to 0
    cents = int(input("Insert Cents: "))
    #user le input gareko coin yedi 25 10 wa 5 xa vane matrai coke bata tyo input gareko value gataune
    if cents == 25 or cents == 10 or cents ==5: #will continue to loop until the value of coke reaches 0
        coke=coke-cents
    print("Amount Due: ",+coke)
print("uh, you finally paid it")
