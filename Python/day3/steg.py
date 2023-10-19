#!/usr/bin/env python3

def steg_encode_char(char, cover):
    charbi = format(ord(char), '0>8b')
    for index in range(0,le(cover)):
        coverbinl = list(format(int(cover[index]), '0>8b'))
        coverbinl[-1] = charbin[index]
        cover[index] = str(int(''.join(coverbinl),2))

    pass

def steg_decode_char(stego):
    pass

if __name__ == '__main__':
    pass
