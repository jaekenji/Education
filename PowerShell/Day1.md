## Day 1

### Login
```
xfreerdp /u:student /v:10.50.40.235 -dynamic-resolution +glyph-cache +clipboard
```
### Basics
```
get-command
get-verb
get-command -verb get
get-command -noun process

get-eventlog -logname 'windows powershell' -verbose
get-childitem -path c:\users\student\desktop

get-help *-* -examples
update-help
```

### Variables
```
set-variable c 6
or
$c = 6
and
$a, $b, $c = 1, 2, 3
```
