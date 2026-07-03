users={

}
def newusers(a,b):
    users[a]={}
    users[a]["name"]=a
    users[a]["age"]=b


while True:
    a=input("Enter the name:")
    b=int(input("Enter the age:"))
    newusers(a,b)
    print(users)