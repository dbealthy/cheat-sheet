
Source: https://www.youtube.com/watch?v=U1VzcjCB_sY&t=3090s
## On both machines
1. Update and upgrade system `sudo apt update && sudo apt upgrade`
2. [[Hostname|Add/change hostname]]
3. [[Private Network|Create private network]]. Assign ip addresses with 10.0.0.1%d for controllers and 10.0.0.2%d for nodes.
### Containerd
4. Install container runtime `sudo apt install containerd`
5. Create config directory `sudo mkdir /etc/containerd`
6. Create default config `containerd config default | sudo tee /etc/containerd/config.toml`
7. Edit config file, under *runc.options* change *SystemdCgroup* to true
### Disable SWAP 
8. Disable `sudo swapoff -a`
9. Remove swap `sudo rm /swap.img`
10. Edit `/etc/fstab`
11. Comment line with 
```
/swap.img       none    swap    sw      0       0
```
### Enable bridging 
12. Edit `/etc/sysctl.conf`
13. Uncomment line with `net.ipv4.ip_forward=1` 
### Enable bridge netfilter
14. Edit `/etc/modules-load.d/k8s.conf`
15. add `br_netfilter` at the top
