employees = ("John","Alice","Jared","Lucis")
user = input("Enter Name: ")
try:
    if user in employees:
        print("Welcome," +user)
    else:
        print(("You are not in our system"))
except SyntaxError:
    print("Invalid Character")

