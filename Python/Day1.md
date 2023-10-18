## Day 1

### Simple Casting

```
#!/usr/bin/python3

whosName = input("your name:\t")
print("Hello " + whosName + "!")
whosYear = int(input("year of birth:\t"))
whosAge = str(2023 - whosYear)
print("wow " + whosName + " you MIGHT be " + whosAge + "!")
```

### Lists and Ping

```
#!/usr/bin/python3

import os
 
susIP = input("Enter an IP:\t")
print("Starting ping scan on " + susIP)
lastDot = susIP.rfind(".")
susIP = susIP[0:lastDot + 1]

for i in range(1, 255):
    IP = susIP + str(i)
    response = os.system("ping -c 1 -w 1 " + host + " >/dev/null")
 
    if response == 0:
        print(IP + " is active")
    else:
```
