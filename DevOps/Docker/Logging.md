Print logs disk usage of all docker containers with total
> `sudo du -ch $(docker inspect --format='{{.LogPath}}' $(docker ps -qa)) | sort -h`


Logs are stored in:
`/var/lib/docker/containers/[container-id]/[container-id]-json.log`


## Configure logging driver and rotation

Edit: `/etc/docker/daemon.json`

```json
{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "10"
  }
}
```

Reload docker daemon
```bash
sudo systemctl daemon-reload
sudo systemctl restart docker
```
