NETWORK RECONNAISSANCE
```
question outcomes:
1 what are some items of interest when performing internal/external reconnaissance?
2 what are passive methods used for network reconnaissance?
3 what are active methods used for network reconnaissance?
4 what are best practices for network scanning and enumeration?
5 what are some scanning tools and methods?

objectives:
1 real-time network scanning
2 analysis of network scanning results
```
QUESTIONS
```
1

                      active
         ping scans     |  arp requests
         port scans     |  dns queries
                        |  ping scans
                        |  port scans
                        |
external ---------------|--------------- internal
         dns queries    |  packet sniffing
         whois queries  |  situational awareness
         shodan         |
         google-fu      |
                        |
                     passive


2 passive reconnaissance
  ~ gathering information about targets without direct interaction

3 active reconnaissance
  ~ where am i?: uname -n / hostname 
  ~ who am i?: whoami / id
  ~ who else is on here?: who / w
  ~ what am i allowed to do?: sudo -l
  ~ what ports are open?: netstat -anlptu / ss -nlptu
  ~ are there any special services running?: ps -elf
  ~ what interfaces do i have?: ifconfig / ip addr (ip a)
  ~ what other hosts does this box know?: arp -a / ip neigh (ip n)
  ~ what routes/networks does this host know?: ip route (ip r)
  nmap: nmap 172.16.82.106 -p- -T4 --min-rate 10000 -A -vvvv - Pn
  nc 
