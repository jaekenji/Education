```
--- PACKET CREATION AND SOCKET PROGRAMMING ---

for today: Network Socket Communication

1 Understanding socket types for network functions
2 Differentiate user space/kernel space sockets
3 Understanding socket creation behavior based on privilege level
4 Implement network programming with Python3

-- 1 SOCKET TYPES --

~ Stream Sockets
  Connection oriented and sequenced

~ Datagram Sockets
  Connectionless

~ Raw Sockets
  Direct sending and receiving of IP packets (no protocols)

-- 2 USER SPACE / KERNEL SPACE SOCKETS

~ User Space (front facing)
  Stream Sockets
  Datagram Sockets

~ Kernel Space
  Raw Sockets

-- 3 SOCKET CREATION --

~ User Space Sockets
  Do not require elevated privileges

~ Kernel Space
  Attempts to access hardware directly

-- 4 PYTHON --
```
```
import socket
  s = socket.socket(socket.FAMILY, socket.TYPE, socket.PROTOCOL)
```
```
socket.socket([*family*[,*type*[*proto*]]])
```
