## Create a new service
Custom services should be stored in ***/etc/systemd/system/*** directory.

```bash
[Unit]
# Type=simple|forking|oneshot|dbus|notify|idle
Description=Telegram registration bot daemon
## make sure we only start the service after network is up
Wants=network-online.target
After=network.target

[Service]
## here we can set custom environment variables
# Environment=AUTOSSH_GATETIME=0
# Environment=AUTOSSH_PORT=0
# By default it's type=simple
# Type=simple|exec|forking|oneshot|dbus|notify|idle
WorkingDirectory=/home/user/Scripts/TG-Registration-Bot
ExecStart=/home/user/Scripts/TG-Registration-Bot/run.sh
# ExecStop=pkill -9 autossh
# don't use 'nobody' if your script needs to access user files
# (if User is not set the service will run as root)
#User=nobody

# Useful during debugging; remove it once the service is working
StandardOutput=console

[Install]
WantedBy=multi-user.target
```



## Commands 
- Basic start/restart
>`systemctl start <ServiceName>`
>`systemctl stop <ServiceName>`
>`systemctl restart <ServiceName>`

- Add service to auto start
> `systemctl enable <ServiceName>`

- Debut service and see its status
> `systemctl status <ServiceName>`

- To list all services and their statuses
> `systemctl list-units --type=service --all`


- To reload configuration files from file system and regenerate dep. tree
> `systemctl daemon-reload`