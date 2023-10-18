PASSIVE NETWORK ANALYSIS
```
1 Discuss best practices for passive network traffic analysis
2 Describe the use of sniffing tools and methods
3 Perform real-time network traffic sniffing
4 Create filters for items of interest when performing packet captures
```
NETWORK FORENSICS 
```
1 Map a network through correlation of relevant network artifacts gathered through reconnaissance and analysis
2 Identify malware types and indicators
3 Identify unknown protocols employing advanced protocol disassembly tools
4 Determine network anomalies through traffic analysis
5 Assess post compromise network behavior
```
```
FINGERPRINTING AND HOST IDENTIFICATION
Variances in the RFC implementation for different OS’s and systems enables the capability for fingerprinting

Tools used for fingerprinting and host identification can be used passively(sniffing/fingerprinting) or actively(scanning)

P0F (PASSIVE OS FINGERPRINTING)
Looks at variations in initial TTL, fragmentation flag, default IP header packet length, window size, and TCP options

Configuration stored in:
 /etc/p0f/p0f.fp

sudo p0f -r <file>.pcap (-o /var/log/p0f.log)(-i <interface>)

sudo cat /var/log/p0f.log | grep "mod=http"
```
```
NETWORK TRAFFIC SNIFFING
What makes traffic capture possible?

Libpcap

WinPcap (outdated)

NPCAP
```
```
tcpdump -r <file>.pcap '<filter> | awk {print $3} | -cut -d. -f1-4 | uniq -c
```
```
NETWORK DATA TYPES
Full Packet Capture Data

~ Session Data
  ~ sflow
  ~ NetFlow

~ Statistical Data
~ Packet String Data
~ Alert Data
~ Log Data
```
```
DATA COLLECTION DEVICES
~ Sensors
  ~ In-Line
  ~ Passive
```
```
METHODS OF DATA COLLECTION
~ TAP
~ SPAN
~ ARP Spoofing (MitM)
```
```
ANOMALY DETECTION
Indicator of Attack (IOA)
~ Proactive
~ A series of actions that are suspicious together
~ Focus on Intent
~ Looks for what must happen
  ~ Code execution. persistence, lateral movement, etc.
```
```
ANOMALY DETECTION 2
Indicator of Compromise (IOC)
~ Reactive
~ Forensic Evidence
~ Provides Information that can change
  ~ Malware, IP addresses, exploits, signatures
```
```
INDICATORS
~ .exe/executable files
~ NOP sled
~ Repeated Letters
~ Well Known Signatures
~ Mismatched Protocols
~ Unusual traffic
~ Large amounts of traffic/ unusual times
```
```
chardet (as if it was cat)
```
