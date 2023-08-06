# Cron jobs
Crontab alows to make schedules for scripts*
To open crontab editor: `crontab -e`

### Format:
\* * * * * python3 /home/user/Scripts/Dir/main.py
 a b c d e

a - minute
b - hour
c - day
d - month
e - day of the week
Generate cron tab schules
https://crontab-generator.org/


Save all users' crontabs in file called $HOSTNAME.txt
```bash
for user in $(cut -f1 -d: /etc/passwd); do echo $user; crontab -u $user -l; echo .; done >> "$HOSTNAME.txt"
```