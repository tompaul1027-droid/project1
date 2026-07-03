import customer_accounts_store as users
def bank():
    i=0
    while i==0:
        a=input("Enter the username:")
        b=input("Enter the password:")

        if a in users.customers:
            if(str(users.customers[a]["password"])==b):
                print("successfully logged in")
                # logic fix: assignment, not comparison
                i=1
                return 1,a
            else:
                print("invalid credentials")
        else:
            print("invalid credentials")
            


def display(a):
    print(f"Welcome {users.customers[a]['name']} to TP bank")
    print("1.withdraw")
    print("2.deposit")
    print("3.check bank balance")
    print("4.add new user")
    print("5.exit")
    d=input("Enter your choice: ")
    # small safety check so text input doesn't crash the program
    if not d.isdigit():
        print("please enter a number from 1 to 5")
        return 0
    d=int(d)
    if d<1 or d>5:
        print("please enter a number from 1 to 5")
        return 0
    return d
 
def withdraw(a):
    f=float(input("enter the amount: "))
    if(f<=users.customers[a]["balance"]):
        users.customers[a]["balance"]= users.customers[a]["balance"]-f
        users.savecustomers()
        print("balance :", users.customers[a]["balance"])
        print("you have successfully completed your transaction")
    else:
        print("you have insufficient balance")
        print("="*48)
    
def deposit(a):
    f=float(input("Enter the amount:"))
    users.customers[a]["balance"]=  f + users.customers[a]["balance"]
    users.savecustomers()
    print("balance:", users.customers[a]["balance"])

def checkbankbalance(a):
    print("Your current balance is :",users.customers[a]["balance"])

c,a= bank()

while True:
    if(c==1):
         e=display(a)
         print("="*48)
    if(e==1):
        withdraw(a)
        print("="*48)
    if(e==2):
        deposit(a)
        print("="*48)
    if(e==3):
        checkbankbalance(a)
        print("="*48)
    if(e==4):
        users.newuser()
        print("="*48)
    if(e==5):
        print(f"bye bye  {users.customers[a]['name']}")
        print("="*48)
        break








