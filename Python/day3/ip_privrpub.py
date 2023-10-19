#!/usr/bin/python3

from ipaddress import ip_address
   
def IPAddress(IP: str) -> str:
    return "Private" if (ip_address(IP).is_private) else "Public"
     
if __name__ == '__main__' : 
   
    while True:
        print(IPAddress(input('Input IP: ')))
