ACCESS CONTROLS
```
questions to answer:
1 what are differences among traffic filtering methods and technologies?
2 how can we Understand Host Based Filtering, including:
  ~ Configuring iptables
  ~ Configure nftables
3 Understand Network Based Filtering
4 Interpret Cisco Access Control List (ACL)
5 Understand Intrusion Detection or Prevention Systems
```
```
WHAT ARE DIFFERENCES AMONG TRAFFIC FILTERING METHODS AND TECHNOLOGIES?

WHY FILTER TRAFFIC?

Block malicious traffic
Decrease load on network infrastructure
Ensure data flows in an efficient manner
Ensure data gets to intended recipients and only intended recipients
Obfuscate network internals

PRACTICAL APPLICATIONS FOR FILTERING

Network Traffic - allow or block traffic to/from remote locations.
Email addresses - to block unwanted email to reduce risk or increase productivity
Computer applications in an organization environment - for security from vulnerable software
MAC filtering - also for security to allow only specific computers access to a network

WHAT ARE NETWORK TRAFFIC FILTERING CONCEPTS?

DEFAULT POLICIES
Explicit - if stated, given
Implicit - if not stated, but still given

BLOCK-LISTING VS ALLOW-LISTING
Block-Listing (Formerly Black-List)
~ Implicit ACCEPT
~ Explicit DENY

Allow-Listing (Formerly White-List)
~ Implicit DENY
~ Explicit ACCEPT

DISCUSS FILTERING DEVICE TYPES
https://git.cybbh.space/net/public/raw/master/modules/networking/slides-v4/images/T1_Filtering_Devices_Mechanisms&Layer.jpg

FIREWALL FILTERING METHODS
Stateless (Packet) Filtering (L3+4) (ip and ports only)
Stateful Inspection (L4) 
Circuit-Level (L5)
Application Layer (L7)
Next Generation (NGFW) (L7)
```
