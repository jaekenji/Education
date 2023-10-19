#!/usr/bin/python3

import operator as op

print("\n     .....     The Number Finder     .....     \n")

while True:
    string = list(input("               input a string: "))
    numbers = []
    num_list = list(range(0,10))
    for n in string:
        if n in num_list:
            numbers.append(n)
    for i in numbers:
        result = str(op.countOf(numbers,i))
        print(result + '  "' + i + '"' + "'s   found!")
