### 16
```
if [[ -d ~/.ssh ]]; then
  mkdir ~/SSH
  cp -a ~/.ssh/ ~/SSH
else
  echo Run ssh-keygen
fi
```
### 17
```
default_gateway=$(ip route | egrep default | cut -d' ' -f1)
pi=$(which ping)
response=$($pi ic 6 $default_gateway | grep '6 received' | cut -d, -f2 | cut -d" " -f2-3)

if [[ $response == '6 received' ]]; then
  echo successful
else
  echo failure
fi
```
### 18
```
