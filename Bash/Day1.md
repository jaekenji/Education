## Day 1

### site:cht.sh (cheat sheet)

#### Brace expansion
mkdir test{1..5} (makes test1-test5) or test{1..3}.log (makes mult .log directories)

```
01 mkdir ~/11{23,34,45,56}

01.2 touch file ~/1123/{1..5}.txt ~/1123/{6..9}~.txt

01.3 find ~/1123/*.txt

01.3 find ~/1123/*.txt | grep -v "~"

02 find ~/1123 ! -name "*~*" -name "*.txt" | xargs cp -t ~/CUT

03 find /var -empty -printf "%i %f\n"

04 find / -inum 4026532575 -printf '%f\n'
