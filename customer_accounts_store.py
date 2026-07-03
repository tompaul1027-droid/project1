customers={
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
def newuser():

    a=input("Enter the name:")
    b=input("enter the password:")
    c=int(input("Enter bank balance:"))
    customers[a]={}
    customers[a]["name"]=a
    customers[a]["passoword"]=b
    customers[a]["bank balance"]=c

print(customers)