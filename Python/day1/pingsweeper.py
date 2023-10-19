#!/usr/bin/python3

import os
 
susIP = input("Enter an IP:\t")
print("Starting ping scan on " + susIP)
lastDot = susIP.rfind(".")
susIP = susIP[0:lastDot + 1]

for i in range(1, 2):
    IP = susIP + str(i)
    response = os.system("ping -c 1 -w 1 " + IP + " >/dev/null")
 
    if response == 0:
        print(IP + " is active")
    elif response == 1:
        print(IP + " isnt active")
print("DONE!\n")
option = input("Would you like to conduct a portscan? [y/n] ")
if option == "y" or "yes" or "Y":
    ipNumber = input("Which ip [] would you like to conduct a portscan on")
elif option == "n" or "no" or "N":
    print("ok")
