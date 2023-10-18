### Answers

```
egrep '([0-9]{1,3}\.){3}[0-9]{1,3}' StoryHiddenIPs | sort | uniq -c | sort -nr

awk -F: '($3 > 3)&&($NF == "/bin/bash") {print $0}' passwd
