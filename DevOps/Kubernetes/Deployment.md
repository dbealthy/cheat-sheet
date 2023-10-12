
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
sudo kubeadm join 10.0.0.10:6443 --token 39v4pr.8brtno2noi0k1bt4 \
	--discovery-token-ca-cert-hash sha256:fd42e19e58f15f9cee72d71c7cb187445621c50b9e8848219da28f74dd095020 \
	--control-plane
```

Join nodes command:
``` bash
sudo kubeadm join 10.0.0.10:6443 --token 39v4pr.8brtno2noi0k1bt4 \
	--discovery-token-ca-cert-hash sha256:fd42e19e58f15f9cee72d71c7cb187445621c50b9e8848219da28f74dd095020
```

To regenerate join commands use if it is timed out:
```
kubeadm token create --print-join-command
```