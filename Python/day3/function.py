#!/usr/bin/python3

import datetime

hour = 0
minute = 0
second = 0
time = 0

def my_function():
    h = int(input("h = "))
    m = int(input("m = "))
    s = int(input("s = "))
    if 0 <= h <= 23 and 0 <= m <= 59 and 0 <= s <= 59:
        t = str((3600000 * h) + (60000 * m) + (1000 * s))
        print("result = " + t)
    else:
        print("Invalid format")
    pass

while True:
    my_function()
