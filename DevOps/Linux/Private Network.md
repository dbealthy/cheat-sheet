In order to create a private network we must create a subnet with private ip addresses on each of server instances, those ip addresses must be in the same mask


1. Go to `cd /etc/netplan`
2. List all files `ls -a`
3. Create a current netplan backup
4. Edit netplan file
5. Either create a separate network interface for private network or use any existing one
6. Add private ip address and mask in the `addresses` section under the network interface name
7. Check and apply settings `sudo netplan --debug apply`


### Example
```yaml
network:
  ethernets:
    ens18:
      addresses:
      - 185.146.1.232/28
      - 10.0.0.10/24  # Private ip address with mask
      nameservers:
        addresses:
        - 195.210.46.195
        - 195.210.46.132
        search: []
      routes:
      - to: default
        via: 185.146.1.225
  version: 2
```