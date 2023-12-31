#!/usr/bin/python3

import socket
import sys
from queue import Queue
import threading
import os

def clear():
 
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')
clear()
    
print('''
_______________     ___________________________   ______   __________________ 
____  _/__  __ \    __  ___/_  ____/__    |__  | / /__  | / /__  ____/__  __ \\
 __  / __  /_/ /    _____ \_  /    __  /| |_   |/ /__   |/ /__  __/  __  /_/ /
__/ /  _  ____/     ____/ // /___  _  ___ |  /|  / _  /|  / _  /___  _  _, _/ 
/___/  /_/          /____/ \____/  /_/  |_/_/ |_/  /_/ |_/  /_____/  /_/ |_||
|                                                                           |
|---------------------------------------------------------------------------|''')

while True:
    IP = input("\n\nEnter Your ip: ")
    host = str(IP)
    dot = IP.rfind(".")
    IP = IP[0:dot + 1]

    normalPortStart = 1
    normalPortEnd = 1024
    allPort = 1
    allPortEnd = 65535
    customPortStart = 0
    customPortEnd = 0

    print("Select your scan type: ")
    print("[+] Select 1 for network scanning")
    print("[+] Select 2 for 1 to 1024 port scanning")
    print("[+] Select 3 for 1 to 65535 port scanning")
    print("[+] Select 4 for custom port scanning")
    print("[+] Select 5 for exit \n")
    
    mode = int(input("[+] Select any option: "))
    print()
    
    if mode == 4:
        customPortStart = int(input("[+] Enter starting port number: "))
        customPortEnd = int(input("[+] Enter ending port number: "))
    
    print("-"*50)
    print(f"Target IP: {host}")

    print("-"*50)
    def scan(port):
        s = socket.socket()
        s.settimeout(5)
        result = s.connect_ex((host, port))
        if result == 0:
           print("port open", port)
        s.close()
    
    queue = Queue()
    def get_ports(mode):
        if mode == 1:
            print("\n[+] scanning.. \n")
            for i in range(1, 255):
                host = IP + str(i)
                response = os.system("ping -c 1 -w 1 " + host + " >/dev/null")
                if response == 0:
                    print(host + " is up")
                else:
                    print(host + " is down")
        elif mode == 2:
            print("\n[+] scanning..\n")
            for port in range(normalPortStart, normalPortEnd+1):
                queue.put(port)
        elif mode == 3:
            print("\n[+] scanning..\n")
            for port in range(allPort, allPortEnd+1):
                queue.put(port)
        elif mode == 4:
            print("\n[+] scanning..\n")
            for port in range(customPortStart, customPortEnd+1):
                queue.put(port)
        elif mode == 5:
            print("[-] Exiting...")
            sys.exit()
    
    open_ports = [] 
    def worker():
        while not queue.empty():
            port = queue.get()
            if scan(port):
                print("Port {} is open!".format(port))
                open_ports.append(port)
    
    def run_scanner(threads, mode):
    
        get_ports(mode)
    
        thread_list = []
    
        for t in range(threads):
            thread = threading.Thread(target=worker)
            thread_list.append(thread)
    
        for thread in thread_list:
            thread.start()
    
        for thread in thread_list:
           thread.join()
    
    run_scanner(1021, mode)
