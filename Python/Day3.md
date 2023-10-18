## Day3

### Inverted

```
#!/usr/bin/env python3

def invert(l):

    '''
    #from 0 to the length of the list
    for n in range(0, len(l)):
        #subtract that current list value
        l[n] = str(255 - int(l[n])
    '''

    #ORRR

    '''
    #start new counter
    counts = 0
    #for each item in l
    for num in l:
        #subtract cuurent l value
        l[counts] = str(255 - int(num))
        counts += 1
    '''

    pass

def inverted(l):

    '''
    result = []
    for n in l:
        result.append(str(255-int(n)))
    return result
    '''

    return [str(255 - int(n)) for n in l]


    pass

if __name__ == '__main__':
    pass
```

### Stego

```
#!/usr/bin/env python3

def steg_encode_char(char, cover):
    #gets the raw binary of char
    charbin = format(ord(char), '0>8b')
    #cover is a list, so for every object
    #in the list
    for index in range(0,len(cover)):
        #
        coverbinl = list(format(int(cover[index]), '0>8b'))
        coverbinl[-1] = charbin[index]
        cover[index] = str(int(''.join(coverbinl),2))

    pass

def steg_decode_char(stego):
    #create an empty list
    msgbits = []
    #stego is a list
    for b in stego:
        #append the binary b to the end of the msgbits list
        msgbits.append(bin(int(b))[-1])
    #retuns a character after msgbits was reassembled
    return chr(int(''.join(msgbits),2))
    pass

if __name__ == '__main__':
    pass
```

### Reading files

```
p_words = []
with open("file.txt") as fp:
    lines = fp.read()
    for i in line.split():
        if 'p' in i:
            p_words.append(i)
```
