### Fundamentals
```
## Understandings:

Networking Fundamentals
~ OSI Model and Networking

Common Protocol Headers
~ Implied security in headers

Layer 2 Technologies (Switching)
~ What is switching and the CAM table?

Layer 3 Technologies (Routing)
~ What is routing?
~ What are routing tables?
~ What is HSRP and VRRP
~ What is static/dynamic routing
~ What is BGP and how does it operate
~ What are some implied security and mitigations for routing?
```
#### OSI Model
```
1 Physical Layer
  ~ Radio
  ~ Cables
  ~ Phone
2 Data Link
  ~ ARP
  ~ LAN/MAN/WAN
3 Network
  ~ IPv4/IPv6
  ~ ICMP/ICMPv6
  ~ RIP/EIGRP/OSPF/IS-IS/BGP
4 Transport
  ~ TCP/UDP
5 Session
  Use for maintaining session based streams
  ~ Netbios
6 Presentation
  All encoding, formating, compression, etc. happens
  ~ Most file types
7 Application
```
##### 1 Physical
```
```
##### 2 Data Link
```
MAC (Media Access Control)
LLC (Logical Link Control)

Ethernet Headers

Type II Frame
--
Destination MAC   |   Source MAC   |   Ethertype  ||  Payload  |  CRC/FCS  |

DMAC                  SMACS  the next  ETHERTYPE
--

Ethertypes:
0x0800 IPv4
0x0806 ARP
0x86DD IPv6
0x8100 VLAN Tag

802.1Q Header
--
Destination MAC   |   Source MAC   |   VLAN  Tag  |  Ethertype  ||  Payload  |  CRC/FCS  |
                                 /                  \
                               /                      \
                              | Tag ID | QoS | VLAN ID |
--

ARP Header
![ARP_Header](https://github.com/jaekenji/Networking/assets/140440974/8174fa35-4d62-4ae0-8874-1316d29c322f)

With ARP, there are some security concerns
Gratuitous ARP (you have to be on the network)
other...
```
##### 3 Network
```
IPv4 Header
--
First 4 Bytes
|  Version  |  IHL  |  DSCP  |  ECN  |  Total Length  |

Next 4 Bytes
|  Identification  |  Flags  |  Fragment Offset  |

Next 4 Bytes
|  Time to Live  |  Protocol  |  Header checksum  |
                /              \
               | TCP, UDP, ICMP |

Next 4 .. .. ..
|  Source IPv4  |
|  Destin IPv4  |
|  Options if IHL > 5 |
--

Fragmentation occurs when the packet size exceeds an MTU

|  RES  |  DF  |  MF  |  Offset  |  Data .....  |

( MTU - IHL ) / 8 = Offset


IPv6 Header
--
First 4 Bytes
|  Version  |  Traffic Class  |  Flow Label  |

Next 4 Bytes
|  Payload Length  |  Next Header  |  Hop Limit  |

Next 16 Bytes .. ..
|  Source IPv6  |
|  Destin IPv6  |
--

IPv6 doesnt fragment, instead send echo saying packet too large

Some security concerns:
Fingerprinting TTL and TCP window size


ZERO CONFIGURATION

IPv4 Auto Config
* APIPA
* RFC 3927

IPv6 Auto Config
* SLAAC (Stateless Address Auto-configuration)
*RFC 4862
```
##### 4 Transport
```
TCP Header
--
First 4 Bytes
|  Source Port  |  Destin Port  |

Next 4 Bytes .. .. 
|  Sequence Number |
|  Acknowledgement Number  |

Next 4 Bytes
|  Offset  |  Reserved  |  TCP Flags  |  Windows  |

Next 4 .. ..
|  Checksum  |  Urgent Pointer  |
|  TCP Options  |
--

In order to establish connection SYN, SYN+ACK, ACK
Send over connection PSH, PSH+ACK
Terminate connection FIN, FIN+ACK, FIN, FIN+ACK

UDP Header
--
First 4 Bytes .. ..
|  Source Port  |  Destin Port  ||  Length  |  Checksum  |
--
```
##### 5 Session
```
Protocols
~ SOCKS 1080
~ NetBIOS SMB CIFS (UDP 137/138 or TCP 139/445)
~ PPTP 1723
~ L2TP 1701
~ RPC (Any port)
```
##### 6 Session
```
Responisbile for:
~ Translation
~ Formating
~ Encoding
~ Encryption
~ Compression
```
##### 7 Presentation 
```
FTP (TCP 20/21)
How do you get your pizza?
Modes Active or Passive

With this being said, you cant Active FTP in SSH tunnel

40,0,0,196,160(X256),(+)46

SSH (22)
Asymmetric for encrypting session
Symmetric is the session key

Overall Architecture
~ Server
~ Client
~ Session
~ Keys
  ~ User Key / Host Key: Asymmetric Public Keys
  ~ Session Key: Symmetric Key created by the client
~ Known-Hosts
~ Agent
~ Signer
~ Random Seed
~ Config file

TELNET (23)
Insecure shell

SMTP (25)
Mail

TACACS (TCP 49)

HTTP(S) (TCP 80/443)
~ GET / HEAD / POST / PUT
~ 100 200 300 400 500

POP (110)
Post Office Protocol

IMAP (143)
Internet Message Access Protocol

RDP (3389)
Remote Desktop Protocol

DNS (TCP/UDP 53)
Name Query or Zone Transfers

DHCP (UDP 67/68)
Dynamic Host Configuration Protocol
Client 68 -> Server 67
Discover, Offer, Request, Acknowledge

TFTP (UDP 69)

NTP (UDP 123)

SNMP (UDP 161/162)

RADIUS (UDP 1645/1646 AND 1812/1813)

RTP (UDP ANY ABOVE 1023)
```
##### Switches
```
~ Fast Forward - Only Destination MAC
~ Fragment Free - First 64 bytes
~ Store and Forward - Entire Frame and FCS

CAM tables
~ MAC to Ports

SPANNING TREE PROTOCOL (STP)
Root decision process
~ Elect root Bridge
~ Identify the Root ports on non-root bridge
~ Identify the Designated port for each segment
~ Set alternate ports to blocking state

Cisco Discovery Protocol (CDP)
Foundry Discovery Protocol (FDP)
Link Layer Discovery Protocol(LLDP)

DTP (Dynamic Trunking Protocol)

VTP (VLAN Trunking Protocol)
for any devices that need to be vlan aware, we can tell it "you are carrying these vlans"
now vlans can communicate with other vlans
```
##### Routing
```
~ Routing tables

Picks Longest Match
