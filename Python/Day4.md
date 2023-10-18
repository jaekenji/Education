## Day 4

### String[start:stop:step}

```
my_string = "123456789"

my_string[::-1]

#output:
#"987654321"

mystring[::3]

#output
#"147"

my_string[2::3]

#output
#"369

my_text = "Hello World! What a wonderful day."

#default split is on space
text_list = list(my_text.split())



with open("file1.txt", "r") as file1, open("file2.txt", "w") as file2:
  data = file1.read()
  file2.write(data)
#read all the contents ofe file1 and writes the to file2

our_set = {1,2,3,4,5,6,100,7,8,9}
another_set = {9,4,-1,-6,45,100,13,2}

our_set.difference(another_set}
our_set.union(another_set)

######


our_dict = {'Brandon':25, 'Josh':22, 'Sarah':32}

our_dict[Brandon]
#prints 25

for key in our_dict:
  print(f"hello {key} you are {our_dict[key]} years old")

#prints
#hello Brandon you are 25 years old
#hello Josh you are 22 years old
#hello Sarah you are 32 years old

del our_dict['Josh']
#deletes josh and value

our_dict['Zeek'] = 24
#adds zeek and assigns 24 as value

######

random_string = input("enter random string: ")

my_dict = {}

for item in random_string:
  if item in my_dict:
    my_dict[item] += 1
  else:
    my_dict[item] = 1
print(my_dict)



