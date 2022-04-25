# Linux services
## Create a new service
Custom services should be stored in ***/etc/systemd/system/*** directory.
[[Linux service example|Service structure example]]
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
- > `systemctl list-units --type=service --all`

