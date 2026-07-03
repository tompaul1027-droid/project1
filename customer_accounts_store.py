import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("customers.json")

default_customers={
    "thomas":{
        "name":"thomas",
        "password":1234,
        "balance":1000
        },
    "achu":{
        "name":"achu",
        "password":"top",
        "balance":8900
        },
    "paul":{
        "name":"paul",
        "password":"hi",
        "balance":100000
        },
    "sachu":{
        "name":"sachu",
        "password":'helo',
        "balance":100000
        
        }
    }


def loadcustomers():
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            pass
    return default_customers.copy()


def savecustomers():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(customers, f, indent=4)


customers = loadcustomers()

def showcustomers():
    print("\n" + "="*48)
    print("CUSTOMER DETAILS")
    print("="*48)
    print(f"{'Username':<15}{'Name':<15}{'Password':<10}{'Balance':>8}")
    print("-"*48)

    for username, data in customers.items():
        password = str(data["password"])
        masked_password = "*" * len(password)
        print(f"{username:<15}{data['name']:<15}{masked_password:<10}{data['balance']:>8}")

    print("="*48)

def newuser():

    a=input("Enter the name:")
    b=input("enter the password:")
    c=int(input("Enter bank balance:"))
    customers[a]={}
    customers[a]["name"]=a
    # logic fix: use the same keys used everywhere else in bank_management_cli
    customers[a]["password"]=b
    customers[a]["balance"]=c
    savecustomers()
    # show data in a clean table format instead of raw dictionary
    showcustomers()

if not DATA_FILE.exists():
    savecustomers()

showcustomers()