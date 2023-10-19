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
