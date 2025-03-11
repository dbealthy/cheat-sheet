Mount shared dir in guest
```bash
sudo mount -v -t virtiofs host_shared host-shared`
```

or mount on system startup

`vim /etc/fstab`
```
host_shared /home/kali/host-shared virtiofs defaults,_netdev 0 0
```

Test
```bash
sudo mount -a
```