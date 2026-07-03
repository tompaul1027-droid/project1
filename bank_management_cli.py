import customer_accounts_store as users
def bank():
    i=0
    while i==0:
        a=input("Enter the username:")
        b=input("Enter the password:")

        if a in users.customers:
            if(str(users.customers[a]["password"])==b):
                print("successfully logged in")
                i==1
                return 1,a
        else:
            print("invalid creditionals")
            


def display(a):
    print(f"Welcome {users.customers[a]["name"]} to TP bank")
    print("1.withdraw")
    print("2.deposit")
    print("3.check bank balance")
    print("4.add new user")
    print("5.exit")
    d=int(input("Enter your choice: "))
    return d
 
def withdraw(a):
    f=float(input("enter the amount: "))
    if(f< users.customers[a]["balance"]):
        users.customers[a]["balance"]= users.customers[a]["balance"]-f
        print("balance :", users.customers[a]["balance"])
        print("you have successfully completed your transaction")
    else:
        print("you have insufficient balance")
    
def deposit(a):
    f=float(input("Enter the amount:"))
    users.customers[a]["balance"]=  f + users.customers[a]["balance"]
    print("balance:", users.customers[a]["balance"])

def checkbankbalance(a):
    print("Your current balance is :",users.customers[a]["balance"])

c,a= bank()

while True:
    if(c==1):
         e= display(a)
    if(e==1):
        withdraw(a)
    if(e==2):
        g= deposit(a)
    if(e==3):
        h=checkbankbalance(a)
    if(e==4):
        users.newuser()
    if(e==5):
        print(f"bye bye  {users.customers[a]["name"]}")
        break





