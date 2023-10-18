```

Time for the test

~~~

[+] Main Guide
https://os.cybbh.io/public/os/latest/index.html

~~~

[+] Windows Persistence

- schtasks

- PowerShell Profiles
  - Order of execution
    - AllUsersAllHosts
    - AllUsersCurrentHost
    - CurrentUserAllHosts
    - CurrentUserCurrentHost

- Ports
  - netstat -ano / -antp

- Processes
  - Tasklist
  - Get-Process
  - Get-Service
  - AutoRuns

- Registry
  - HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run(Once)
  - HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run(Once)
  - HKLM\SYSTEM\CurrentControlSet\Service
  - HKCU\SYSTEM\CurrentControlSet\Service
Anything for Registry USE GUI !! regedit/autoruns

- Prefetch is NOT persistence

~~~

[+] Linux Persistence

- Ports
  - netstat -ano / -antp

- Processes
  - ps -elf / -forest
  - top
  - htop

- Persistence locations
  - /etc/inittab
  - /etc/cron
  - ~/.profile
  - ~/.bashrc

```
