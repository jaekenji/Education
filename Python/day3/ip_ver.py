#!/usr/bin/python3

yes = " ...IS a private address!\n"
no = " is ...NOT a private address!\n"
x = 1
while x:
    IP = input("Enter a valid IP address: ")
    octetList = IP.split(".")
    validIP = int(len(octetList))
    if validIP != 4:
        print(IP + " ......really dude ._.\n")
        continue

    x = int(octetList[0])
    y = int(octetList[1])
    w = int(octetList[2])
    z = int(octetList[3])
    
    if 0 < x < 255 and 0 <= y <= 255 and 0 <= w <= 255 and 0 <= z <= 255:
        if x == 10:
            print(IP + yes)
        elif x == 172:
            if 16 <= y <= 31:
                print(IP + yes)
            else:
                print(IP + no)
        elif x == 192:
            if y == 168:
                print(IP + yes)
            else:
                print(IP + no)
        else:
                print(IP + no)
    else:
        print(IP + " ......really dude ._.\n")
