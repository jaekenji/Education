#!/usr/bin/python3
import operator as op
print("\n     .....     Character Counter     .....     \n")
char_set = list(input("            please input string: "))
for c in char_set:
    count = op.countOf(char_set,c)
    if count == 1:
        print(c + " appeared 1 time.")
    else:
        print(c + " appeared " + str(count) + " times.")
