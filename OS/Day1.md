# OS

## Day 1

Basics
```
get-command -type cmdlet | sort noun | ft commandtype,name,version,source
get-help get-alias
get-history

(get-process).name
get-process | select-object name
get-process | get-member | where-object {$_.membertype -match "method"}
get-process | select-object name,id,path | where-object {$_.id -lt '1000'}
                                                         (                ).count
```

CIM
```
get-cimclass
get-ciminstance -classname win32_logicaldisk
```

Execution Policy
```
get-executionpolicy -list
# as normal 'Windows Policy' there is policy for executing programs
# USMC has default execution policy
set-executionpolicy -executionpolicy unrestricted -scope currentuser
```

#### Profile Types

AllUsersAllHosts
AllUsersCurrentHost
CurrentUserAllHosts
CurrentUserCurrentHost
```
test-path -path $profile.<profiletype>
```

Persistence
```
can embed downloader inside of powershell profile
```


## Day 2

### The Registry

```
"C:\Windows\regedit.exe"
"C:\Windows\System32\reg.exe"
```
also can view remote registries
~
Open the Regedit GUI
Click on *File* => *Connect Network Registry*
Type *File-Server*
Click on *Check Names* Button (File-Server will become underlined)
Click *OK*
~

Registry changes usually require a restart before they take effect


#### Registries

- HKEY_LOCAL_MACHINE
    - system level
      
- HKEY_CURRENT_CONFIG
    - resides in RAM
    - (symbolic link to the user on a system)
  
- HKEY_USERS
    - where each user (whos logged in) config data is store
    - S-1-5-18	Local System
    - S-1-5-19	NT Authority	Local Service
    - S-1-5-20	NT Authority	Network Service
    - S-1-5-21domain-500 Administrator
      
- HKEY_CURRENT_USER
    - who ever is not logged on 
      
- HKEY_CLASSES_ROOT
  

Key > Value Name > Value Data

Every key is read from the top down, and the configuration is applied to the system
Hive Keys are

reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run <# KEY #> /v <# PATH #> /t <# TYPE #> /d <# DATA #>

### Powershell

```
new-item HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\runagain
new-item property HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\runagain\ -name Test -propertype string -value c:\windows\system32\windowspowershell\v1.0\powershell.exe

get-psdrive

new-psdrive -name "Public" -psprovider "FileSystem" -root "\\Server01\Public"
```


## Day 3

## Day 4

### Logon Process from NTOS

- NTOSKERNEL.EXE
    - SMSS.EXE (master session manager)
        - CSRSS.EXE(0) (windows sub system process)
          ##### User Mode
            - Kernel32.dll
            - User32.dll
            - GDI32.dll
            - ADVAPI32.dll
            - KernelBase.dll
          ##### Kernel Mode
            - WIN32K.SYS
            - Conhost.exe
              
    - WINNIT.EXE
        - SERVICES.EXE(0) (Service Control Manager SCM)
            - starts all services with 0x2
        - LSASS.EXE(0) (Local Security Authority Sub System LSA)
            - authentication packages
    - SMSS.EXE(1)
        - CSRSS.EXE(1)
            - all dependencies
        - Winlogon.exe(1)
            - LogonUI.exe
            - Userinit.exe
                - Explorer.exe

## Day 5

### Process Validity

```
get-process

get-process | sort id
get-process | select name,id,description | sort id

get-process smss, csrss, lsass | sort id

get-process chrome | foreach {$a} {$_.modules} | more

get-process *chrome* | select -expandproperty modules
```

## Day 6 

### idk yet

```
ps -elf
htop
```

Every user space process stems from /sbin/init ( PID of 1 )
Every kernel space process stems from [kthreadd] ( PID of 2 )

##### User v Kernel space
Kernel runs with its own memory (no allocation or set space) and is unrestricted,
SO for user mode processes not to mess with Kernel, User is dedicated space

d             rwx           rwx           rwx
file type     own privs     group privs   others privs

### System Calls

fork() - creates same instance of that process

exec() - starts program, replacing itself

~

```
ps -elf | head -n5SIGSTOP

ps --ppid 2 -lf | head
ps -elf --forest
```
## Day 8 

##### Artifacts

Objects or areas within a computer system that have important information related to the activities performed by the computer user
Most artifacts will require sids to view
```
Get-LocalUser | select Name,SID
```
-----
#### UserAssist

Keeps track of GUI programs that were ran by user

~ For exe s ran ~
```
Get-ItemProperty 'REGISTRY::HKEY_USERS\*\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{CEBFF5CD-ACE2-4F4F-9178-9926F41749EA}\Count'
```

~ For shortcuts ran ~
```
Get-ItemProperty 'REGISTRY::HKEY_USERS\*\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{F4E57C4B-2036-45F0-A9AB-443BCFE33D9F}\Count'
```
-----
#### Windows Background Activity Moderator

Kinda the same as UserAssist, but for background processes ran
```
Get-Itemproperty 'HKLM:\SYSTEM\CurrentControlSet\Services\bam\UserSettings\*' (Windows 1709 & 1803)
```
```
Get-Itemproperty 'HKLM:\SYSTEM\CurrentControlSet\Services\bam\state\UserSettings\*' (Windows 1809 and newer)
```
-----
#### Recycle Bin

Self-explanatory
Used in many forensic investigations
```
gci 'C:\$RECYCLE.BIN' -Recurse -Verbose -Force | select *
```
```
gci 'C:\$RECYCLE.BIN' -Recurse -Force
```
-----
#### Prefetch

Prefetch is a type of file that gets created when an application is run for the FIRST time
```
gci -Path 'C:\Windows\Prefetch' -ErrorAction Continue | select * | select -first 5
```
-----
#### Jump Lists

Jumplists are links to items the user has accessed frquently FROM a specific item
```
gci -Recurse C:\Users\*\AppData\Roaming\Microsoft\Windows\Recent -ErrorAction Continue | select FullName, LastAccessTime
```
-----
#### Recent Files

The recent tab in winkey popup is made by user reg key to better quality of life for users
stored in reg key
```
gci 'REGISTRY::HKEY_USERS\*\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs'
```

~ Hex to Unicode ~
```
[System.Text.Encoding]::Unicode.GetString((gp "REGISTRY::HKEY_USERS\*\SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.txt")."0")
```

~ All Hex to Unicode ~
```
Get-Item "REGISTRY::HKEY_USERS\*\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.txt" | select -Expand property | ForEach-Object { [System.Text.Encoding]::Default.GetString((Get-ItemProperty -Path "REGISTRY::HKEY_USERS\*\Software\Microsoft\Windows\CurrentVersion\Explorer\RecentDocs\.txt" -Name $_).$_)}
```
-----
#### Browser Artifacts

All browser history including the following: navigation history, bookmarks, downloaded file list, cache data
```
.\strings.exe 'C:\Users\<username>\AppData\Local\Google\Chrome\User Data\Default\History'
```

Find FQDNs
```
$History = (Get-Content 'C:\users\<username>\AppData\Local\Google\Chrome\User Data\Default\History') -replace "[^a-zA-Z0-9\.\:\/]",""
```
```
$History| Select-String -Pattern "(https|http):\/\/[a-zA-Z_0-9]+\.\w+[\.]?\w+" -AllMatches|foreach {$_.Matches.Groups[0].Value}| ft
```

### Auditing
For of logging. An event happens, and it is recorded

## Day 9

### Linux Auditing and Logging

#### Logging

##### What is it?

Any time there is an **Authentication, Users Currently Logged In, Any History of the Previous Log,** and **Failed Authentication Attempts**

```
/var/log/auth.log #Authen
/var/run/utmp #Users Logged
/var/log/wtmp #History of Users Logged
/var/log/btmp #Failed Auth
```

##### Why is it important?

**Historical analysis**
Record of anomalous activity
Diagnostics of a failure

-----

Location : /var/log

Config File : /etc/rsyslog.conf

Service : /usr/sbin/rsyslogd

-----

```
/etc/rsyslog.conf
```

Log entries follow syslog standard **facility.severity**

facility = what program, or part of system, log is from
severity = urgency

the lower the code the bigger the danger


## Day 10

### Contrast privilege levels of local domain groups and accounts

Before diving too much into the woods, its important to baseline good administrator practice, inluding:
- Monitoring all users from highest privilege to least
- Understand group nesting
- View all administrator local logons



```
get-addefaultdomainpasswordpolicy
# ENUMERATE PASSWORD POLICY
```
```
get-adfinegrainedpasswordpolicy -filter {name -like "*"}
# NO RETURN = NOT SET
```
```
get-adforest
# ENUMERATE FOREST DETAILS
```
```
get-adgroup -filter *
# GETS AD GROUPS
get-adgroup -identity 'adgroup'
# GETS GROUP DETAILS
get-adgroupmember -identity 'anotheradgroup'
# GETS LIST OF ADGROUP MEMBERS
```
```
get-aduser -filter 'name -like "*"'
# GETS ALL ADUSERS
get-aduser -filter 'user.name' -properties description
# GETS ALL ADDITIONAL PROPERTIES OF SPECIFIED USER
```

#### Group Nesting

```
(get-adgroupmember -identity 'system admins').name
```

### Use CMD shell to query, view, analyze, modify and create AD Objects

### Use PowerShell to query, view, analyze, modify, and create AD Objects

### Use PowerShell to survey domain controller security posture




