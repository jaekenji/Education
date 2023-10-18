# Prac Exam Notes

### Exam


```
#!/usr/bin/env python3

def q1(floatstr):
    '''
    TLO: 112-SCRPY002, LSA 3,4
    Given the floatstr, which is a comma separated string of
    floats, return a list with each of the floats in the 
    argument as elements in the list.
    '''
    pass

def q2(*args):
    '''
    TLO: 112-SCRPY006, LSA 3
    TLO: 112-SCRPY007, LSA 4
    Given the variable length argument list, return the average
    of all the arguments as a float
    '''
    pass

def q3(lst,n):
    '''
    TLO: 112-SCRPY004, LSA 3
    Given a list (lst) and a number of items (n), return a new 
    list containing the last n entries in lst.
    '''
    pass
    
def q4(strng):
    '''
    TLO: 112-SCRPY004, LSA 1,2
    TLO: 112-SCRPY006, LSA 3
    Given an input string, return a list containing the ordinal numbers of 
    each character in the string in the order found in the input string.
    '''
    pass

def q5(strng):
    '''
    TLO: 112-SCRPY002, LSA 1,3
    TLO: 112-SCRPY004, LSA 2
    Given an input string, return a tuple with each element in the tuple
    containing a single word from the input string in order.
    '''
    pass

def q6(catalog, order):
    '''
    TLO: 112-SCRPY007, LSA 2
    Given a dictionary (catalog) whose keys are product names and values are product
    prices per unit and a list of tuples (order) of product names and quantities,
    compute and return the total value of the order.

    Example catalog:
    {
        'AMD Ryzen 5 5600X': 289.99,
        'Intel Core i9-9900K': 363.50,
        'AMD Ryzen 9 5900X': 569.99
    }

    Example order:
    [
        ('AMD Ryzen 5 5600X', 5), 
        ('Intel Core i9-9900K', 3)
    ]

    Example result:
    2540.45 

    How the above result was computed:
    (289.99 * 5) + (363.50 * 3)
    '''
    pass

def q7(filename):
    '''
    TLO: 112-SCRPY005, LSA 1
    Given a filename, open the file and return the length of the first line 
    in the file excluding the line terminator.
    '''
    pass

def q8(filename,lst):
    '''
    TLO: 112-SCRPY003, LSA 1
    TLO: 112-SCRPY004, LSA 1,2
    TLO: 112-SCRPY005, LSA 1
    Given a filename and a list, write each entry from the list to the file
    on separate lines until a case-insensitive entry of "stop" is found in 
    the list. If "stop" is not found in the list, write the entire list to 
    the file on separate lines.
    '''
    pass

def q9(miltime):
    '''
    TLO: 112-SCRPY003, LSA 1
    Given the military time in the argument miltime, return a string 
    containing the greeting of the day.
    0300-1159 "Good Morning"
    1200-1559 "Good Afternoon"
    1600-2059 "Good Evening"
    2100-0259 "Good Night"
    '''
    pass
    
def q10(numlist):
    '''
    TLO: 112-SCRPY003, LSA 1
    TLO: 112-SCRPY004, LSA 1
    Given the argument numlist as a list of numbers, return True if all 
    numbers in the list are NOT negative. If any numbers in the list are
    negative, return False.
    '''
    pass
```
## Answers
```
newlist = []
for y in floatstr.split(','):
  newlist.append(float(y))
return newlist

# ORR

return [float(X) for x in floatstr.split(',')]

#######

s = 0
for arg in args:
  s += arg
return s/len(args)

#or

return sum(args)/len(args)

########

return lst[-n:]

########

newlist = []
for i in strng:
  newlist.append(ord(i))
return newlist

#OR

return [ord(x) for x in list(strng)]

########

return tuple(strng.split())

#########

#order = [(example)]
#order = [0][0] returns first tuple first item
#order = [0][1] returns first tuple second item

'''Because the way dictionaries work
if you call the name in a dictionary
it returns the value of the item in
the dictionary'''

#catalog = [order[0][0]]
#returns price of order

#SOOOO

total = 0
counter = 0

for x in order:
    total += catalog[order[count][0]] * order[count][1]
return total
#########

with open(filename) as fp:
  x = fp.readline()
  y = len(x) - 1
return y

#########

with open(filename, "w") as fp:
  for w in lst:
    if str.lower(w) != "stop":
      fp.writelines(w + "\n") 
    else:
      break

#########

if miltime in list(range(300,1159)):
  return "Good Morning"
elif miltime in list(range(1200,1559)):
  return "Good Afternoon"
elif miltime in list(range(1600,2059)):
  return "Good Evening"
else:
  return "Good Night"

#########

