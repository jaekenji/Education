#!/usr/bin/env python3
def steg_encode_char(char, cover):

    cover = [250,251,252,251,250,249,248,249]
    char = "a"
    
    charBin = format(ord(char), '0>8b')

    coverBin = format(cover[0], '0>8b')
    
    coverBinList = list(coverBin)

    for s in range(0,8):
        coverBinList = list(format(cover[s], '0>8b'))
        coverBinList[-1] = charBin[s]
        cover[s] = int(''.join(coverBinList),base=2)

    pass

def steg_decode_char(stego):

    msgbits = []
    
    for b in cover:
        msgbits.append(bin(b)[-1])

    chr(int(''.join(msgbits),base=2))

    pass
if __name__ == '__main__':
    pass
