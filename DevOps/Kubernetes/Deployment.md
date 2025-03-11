
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
### Add kubernetes repositories
16. `curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-archive-keyring.gpg`
17. `echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list`
18. `sudo apt update`
### Install tools for kubernetes
18. `sudo apt install kubeadm kubectl kubelet`

## On controller
### Init cluster
1. `sudo kubeadm init --control-plane-endpoint=10.0.0.10 --node-name k8s-controller-0 --pod-network-cidr=10.244.0.0/16`
### Give local user access to manage cluster
2. `mkdir -p $HOME/.kube`
3. `sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config`
4. `sudo chown $(id -u):$(id -g) $HOME/.kube/config`
## Install Flannel overlay network
5. ``` Install to cluster
```bash
kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
```

### Check if cluster is running
6. `kubectl get pods --all-namespaces`

Join controllers command: 
``` bash
 sudo kubeadm join {ip address} --token rwuwno.srsywe558wfriegg \
	--discovery-token-ca-cert-hash {token} \
	--control-plane 
```

Join nodes command:
``` bash
sudo kubeadm join {ip address} --token rwuwno.srsywe558wfriegg \
	--discovery-token-ca-cert-hash {token}
```

To regenerate join commands use if it is timed out:
```
kubeadm token create --print-join-command
```


```
# Please edit the object below. Lines beginning with a '#' will be ignored,
# and an empty file will abort the edit. If an error occurs while saving this file will be
# reopened with the relevant failures.
#
apiVersion: v1
data:
  jws-kubeconfig-96wk06: eyJhbGciOiJIUzI1NiIsImtpZCI6Ijk2d2swNiJ9..WaTVbXHS1rERCVijLAxAHX131BXqFHagUkgIVAomAec
  jws-kubeconfig-acxtlw: eyJhbGciOiJIUzI1NiIsImtpZCI6ImFjeHRsdyJ9..Fwo42ha0TyL4ppKHVfy0HOfuQmlyB8U8fteTVwnF4cM
  jws-kubeconfig-bgroqi: eyJhbGciOiJIUzI1NiIsImtpZCI6ImJncm9xaSJ9..JHRth5xIUL7usodkHqV0XEmcLdJ5W8oi7fMD0Em19Ic
  jws-kubeconfig-ftlaiy: eyJhbGciOiJIUzI1NiIsImtpZCI6ImZ0bGFpeSJ9..MdhffUzp4JQxfNHdoDYoXgCrqu0yh4qLAiFuUtiyy9U
  jws-kubeconfig-wsjawc: eyJhbGciOiJIUzI1NiIsImtpZCI6IndzamF3YyJ9.._WATlDsOaPadvsAH4Uk2tosaCbaie_6kuEzC37PHUnc
  kubeconfig: |
    apiVersion: v1
    clusters:
    - cluster:
        certificate-authority-data: LS0tLS1CRUdJTiBDRVJUSUZJQ0FURS0tLS0tCk1JSURCVENDQWUyZ0F3SUJBZ0lJSldPZThpNmRDYmd3RFFZSktvWklodmNOQVFFTEJRQXdGVEVUTUJFR0ExVUUKQXhNS2EzVmlaWEp1WlhSbGN6QWVGdzB5TXpFeE1qUXhOVEEzTkRSYUZ3MHpNekV4TWpFeE5URXlORFJhTUJVeApFekFSQmdOVkJBTVRDbXQxWW1WeWJtVjBaWE13Z2dFaU1BMEdDU3FHU0liM0RRRUJBUVVBQTRJQkR3QXdnZ0VLCkFvSUJBUUNkKzB0Sk1aRUJXUGZTWmFCZXMxQVZyOFJrMkpSZmJ1aGtDYVNpZWZEc25lZldqVDExOW8xMkVBOVEKbHgvd2V1ZXhtM24vdC9nbExYTHRPMWQzaWd0aVY2OUxVd0QyUmxlNVlvZ05EaHV4Nm5zcnZlYUw4amZ1WExQaAo4eTY5NU9LNks1eEdPTVd1NEhlM3BXbG1mMHdlRlFQYWxKSDJqaDB6dlVBd0prRUowZHBZcElTVWJNMUdneHBNCmthV0tNMlV4bWlBYmVJMENoNm5XWjNDNFVjMXgxQXFCVmk4d2ZPbXlPYXFWK3pkUHRjZWtOVEtZV3YyRTRLQWsKL0JyeWNJTVpOVEhVZjVEeS8yZWpjZzZlZllvMnZMd2gvdkVDRk1hRlBsRnFyKy9nRHp4L3hPU0VvQXZvcTU2VApHeTBGMGVRb01qUjE0Sjl0R3dxdWVTZFFuVk1MQWdNQkFBR2pXVEJYTUE0R0ExVWREd0VCL3dRRUF3SUNwREFQCkJnTlZIUk1CQWY4RUJUQURBUUgvTUIwR0ExVWREZ1FXQkJTQ0JrU3NCUTYyNU5ZNUszRnNGWGswSVV1UElEQVYKQmdOVkhSRUVEakFNZ2dwcmRXSmxjbTVsZEdWek1BMEdDU3FHU0liM0RRRUJDd1VBQTRJQkFRQUZlU0J3RzUxSgplaklZbG1uUi92WVdTTUNRQ1I2WnIrY0FkWkJUZUp2QTFsM0E1ejg4K2l6VzVCVlI5OFB0eTlqbWdMUXJDN0xhCjNSNkU1NzMxeWJraUIxaThzK2ZZenBGVDVjNFdlWWN2K1ZRQUZHVzRVTFRLTndUcTR6emljcERCTDk0TWFaSXQKT0YvZFhrRmYwazBOZG1qWGFKbDBjVVplYVF5L3ltUlJxaE9QQm4vRVJ4cUZwT3J4dUNDOE9SSW9QZ01abnkrSApwSmFkdEJ1TGxneEp3bXMvTmJRT01yMm9rVTNQbDdCNzQ2K1VVN1BQeWRyNnViUFFtYm12a09hZDAvMUdEdzNDCnYyaTRtWHJYcnhiZEhWU1NlNk1hOThoZjNBMmg5QkM3TDV5bGgrZEhOR0xzVUY4SzZxVnorNWdDTjdsL0N4akoKVVJCRmFJczlycEpLCi0tLS0tRU5EIENFUlRJRklDQVRFLS0tLS0K
        server: https://10.0.0.10:6443
      name: ""
    contexts: null
    current-context: ""
    kind: Config
    preferences: {}
    users: null
kind: ConfigMap
                                                            1,1           Top


```