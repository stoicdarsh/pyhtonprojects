balance=float(input("Balance: "))
c_pin=input("Enter Correct Pin: ")
attempt=int(input("Enter Attempt: "))
for i in range(attempt):
    pin=input("Enter pin: ")
    if pin==c_pin:
        break
    else:
            print("Wrong Pin")
            print(f"{attempt-(i+1)} Attempt Left")
else:
    print("Card Blocked")
if c_pin==pin:
    while True:
        print("1. Balance      2. Deposit      3. Withdraw       4. Exit")
        option=int(input("Enter Option[1/2/3/4]: "))
        if option==4:
            print("Thank You!")
            break
        elif option==1:
            print("Balance:",balance)
        elif option==2:
            deposit=float(input("Enter Deposit Momey: "))
            balance+=deposit
            print("Balance:",balance)
        elif option==3:
            while True:
                withdraw=float(input("Enter Withdraw: "))
                if withdraw>balance:
                    print("That much AMount is not Available\n provide from the limited balance...")
                else:
                    balance-=withdraw
                    print("Balance:",balance)
                    break
        else:
            print("Enter From the Given Options...")

