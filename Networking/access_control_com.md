access control commands
```
iptables -t [table] -A [chain] [rules] -j [action]
```
```
### -p icmp [ --icmp-type { type# | code# } ]
-p icmp --icmp-type 0 0 ### reply
-p icmp --icmp-type 8 0 ### request

-p tcp [ --sport | --dport { port1 |  port1:port2 } ]
-p tcp [ --tcp-flags { SYN | ACK | PSH | RST | FIN | URG | ALL | NONE } ]
-p udp [ --sport | --dport { port1 | port1:port2 } ]
```
```
-m state --state [ NEW | ESTABLISHED | RELATED | UNTRACKED | INVALID ]
-m mac [ --mac-source | --mac-destination ] [mac]
-p [tcp|udp] -m multiport [ --dports | --sports | --ports { port1 | port1:port15 } ]
-m bpf --bytecode [ 'bytecode' ] ### berkley packet filter
-m iprange [ --src-range | --dst-range { ip1-ip2 } ]
```
```
-j [ ACCEPT | REJECT | DROP ]
```
```
sudo iptables -L
iptables -A OUTPUT -p tcp -m multiport --ports 22,6010,6011,6012 -j ACCEPT
```
```
sudo nft list ruleset
sudo nft add table ip MyTable
sudo nft list table MyTabe
--
sudo nft add chain ip MyTable Input { type filter hook input priority 0 \; policy accept \;}
sudo nft add chain ip MyTable Output { type filter hook output priority 0 \; policy accept \;}
--
sudo nft add rule ip MyTable Input tcp dport 22 accept
sudo nft add rule ip MyTable Input tcp sport 22 accept

sudo nft add rule ip MyTable Output tcp dport 22 accept
sudo nft add rule ip MyTable Output tcp sport 22 accept
--
sudo nft add rule ip MyTable Input tcp dport {6010,6011,6012} accept
sudo nft add rule ip MyTable Input tcp sport {6010,6011,6012} accept
sudo nft add rule ip MyTable Output tcp dport {6010,6011,6012} accept
sudo nft add rule ip MyTable Output tcp sport {6010,6011,6012} accept
---
sudo nft -f nftrules
---
```
