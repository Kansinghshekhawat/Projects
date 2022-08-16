import time
print("please enter your card ")
time.sleep(5)
passward=000
pin=int(input("please enter your atm pin "))
balance=5000
if pin==passward:
    while True:
        print(""" 1==balance \n 2==widraw balance \n 3==depsit balance\n 4==exit
       
        """)
        try:
            option=int(input("Please enter your choise"))
        except:
            print("please enter valid option ")

        if option==1:
            print(f"your current balance is {balance}")
        if option==2:
            widraw_amount=int(input(f"please enter widraw_amount "))
            balance=balance-widraw_amount
            print(f"{widraw_amount} is debited from your account ")
            print(f"your updated balance is {balance}")
        if option==3:
            deposit_amount=int(input(f"enter yout deposit amount "))
            balance=balance+deposit_amount
            print(f"{deposit_amount} is credited to your account ")
            print(f"your updated balance is {balance}")
        if option==4:
            break
        else:
            print("please enter valid option ")
else:
    print("wrong pin please try again")

