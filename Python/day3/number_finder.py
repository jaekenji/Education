#!/usr/bin/python3

print("\n     .....     The Number String     .....     \n")
print("         1075846403014367439574143167421       \n")

numberString = "1075846403014367439574143167421"
numberString = list(numberString)

while True:
    numbers = list(input("              Input Numbers to Find: "))
    numberFound = []
    for i in numbers:
        result = str(numberString.count(i))
        print(result + '  "' + i + '"' + "'s   found!")
