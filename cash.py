x={}
k={}
while True:
    p=input("""welcome to the SBI
    PRESS 1 FOR REGISTER YOUR SELF FOR ATM
    PRESS 2 FOR CASH DEPOSIT
    PRESS 3 FOR CASH WITDRAWAL
    PRESS 4 BALANCE CHECK
    PRESS 5 FOR EXIT ! 
    """)
    if p=="1":
        print("you register your self......")
        pin=eval(input("enter your NEW PIN"))
        name=input("enter your NAME")
        x[pin]=name




        print("congratulation you register your name and pin:-",x)
    elif p=="2":
        print("you press cash deposite")
        ko=eval(input("enter your PIN"))
        for i in x:
            if i==ko:
                print("you are SBI customer")
                print("welcome mr",x.get(i))
                money=eval(input("enter your amount you deposite"))
                print("thanks for deposite money",x.get(i))
                k[x.get(i)]=money
                print("your deposite amount is:=",k,"ruppes deposite")
            else:
                print("wrong INPUT")
    elif p=="4":
        ko = eval(input("enter your PIN"))
        for i in x:
            if i == ko:
                print("Welcome SBI customer balance check")
                print("welcome mr", x.get(i))
                print("your Current balance is:=", k,"ruppes")
            else:
                print("wrong INPUT")
    elif p=="3":
        ko = eval(input("enter your PIN"))
        for i in x:
            if i == ko:
                print("Welcome SBI cash Withdrwal")
                print("welcome mr", x.get(i))
                wt=eval(input("enter you amount you withdrawal"))
                print("you have withdrawn",wt)
                for j in k:
                    withdrawal=k.get(j)-wt
                    k[j]=withdrawal
                    print(k)
                    print("your current balance is",withdrawal)

                # so=str(s)
                # print(so)
                # lo=x[s]
                # print(lo)
            else:
                print("wrong INPUT")




    elif p=="5":
        print("thanks for using SBI ATM...")
        break
    else:
        print("you press the wrong keyword")