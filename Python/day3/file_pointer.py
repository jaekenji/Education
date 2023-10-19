#!/usr/bin/python3

'''
fp = open("text.txt")
'''

#read
'''with open("test.txt") as fp:
    pass

with open("test.txt", 'r') as fp:
    pass'''

#write
with open("test.txt", 'w+') as fp:
    lines = ['First Line\n', 'Last Line\n']
    fp.write("Hello World!")
    fp.writelines(lines)

    fp.read()

    pass

