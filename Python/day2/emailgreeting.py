#!/usr/bin/python3

while True:

    email = input("Input valid email (first.middle.last@domain.com): ")
    emailList = email.split("@")
    name = str(emailList[0])
    nameList = name.split(".")
    first = nameList[0]
    print("\nGood Afternoon " + first + ", Welcome to " + emailList[1] + "\n")
