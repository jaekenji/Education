## Day 2

### Python Math

```
48/10
#Returns Float

3%2
#Returns 1

2%2
#Returns 0

string = "string"

"This is a {}.format(string)

f"This is a {string}"

#Display variables in strings

IP = "192.168.0.1"

newIP = IP.split(".")

#List of ['192', '168', '0', '1']

".".join(newIP)

#Joins list on "."
```

At home code

```
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
```
### OR
```
ipaddr = input("Input IP: ").split(".")

if ipaddr[0] = "10":
    print("Public")
elif ipaddr[0] = "172" and int(ipaddr[1]) in list(range(16,33)):
    print("Public")
elif ipaddr[0] =
```

Email Greeting

```
#!/usr/bin/env python3

print("\n .....     WELCOME TO GUESS THE NUMBER    ..... \n")
def guess_number(n):
    while True:
        m = int(input("          Guess a number between 1-100: "))
        if m == n:
            print("\n                       WIN!!!\n")
            break
        elif m < n:
            print("\n                      too low\n")
        elif m > n:
            print("\n                      too high\n")
    pass
guess_number(23)
```
