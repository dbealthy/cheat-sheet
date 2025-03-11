



## Repair control pannel

Follow guide from accepted answer:
https://serverfault.com/questions/1065444/how-can-i-find-which-kubernetes-certificate-has-expired


Edit configmap for joining nodes
`kubectl -n kube-public edit configmap cluster-info`

replace 'certificate-authority-data' value with new value generated from current 'ca.crt' `cat /etc/kubernetes/pki/ca.crt | base64 -w 0` 

Get new join command `kubeadm token create --print-join-command
`

## Repair nodes

```bash
kubeadm reset -f
```

````bash
rm -rf /etc/kubernetes/ /var/lib/kubelet/ /var/lib/etcd/
````

Run join command created on controller node server 

`kubeadm join 10.0.0.10:6443 --token ...`


reboot everything