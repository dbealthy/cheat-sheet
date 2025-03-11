# Lounch custom scripts on machine start and restart

```bash
#!/bin/sh
#!/bin/python3

date_time=$(date)
SERVICE="main.py"
if ps -ef | grep "$SERVICE" | grep -v grep >/dev/null
then
    echo "${date_time} main.py is running" >> /home/user/Scripts/VK-Comments-Parser/run.log
else
    echo "${date_time} main.py stopped" >> /home/user/Scripts/VK-Comments-Parser/run.log
    python3 /home/user/Scripts/VK-Comments-Parser/main.py 
fi
```

- Use crontab (python scripts are better to launch from a bash script with[[Crontab]]
- Run script as a Linux service [[Systemd]]
- Use Docker