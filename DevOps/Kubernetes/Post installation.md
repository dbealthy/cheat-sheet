### Install ingress controller
- `helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx`
  
- `helm upgrade --install ingress-nginx ingress-nginx   --repo https://kubernetes.github.io/ingress-nginx   --namespace ingress-nginx --create-namespace`

## Install Load balancer

````bash
helm repo add metallb https://metallb.github.io/metallb
````

``` bash
helm install metallb metallb/metallb --namespace metallb --create-namespace
```

Create config
`vim metallb-config.yaml`

``` yaml
apiVersion: metallb.io/v1beta1
kind: IPAddressPool
metadata:
  name: ip-pool
  namespace: metallb
spec:
  addresses:
	# Assign needed ip range
    - 185.146.1.232/32
    #autoAssign: false 
---
apiVersion: metallb.io/v1beta1
kind: L2Advertisement
metadata:
  name: l2-advert
  namespace: metallb
```

Apply config
`kubectl apply -f metallb-config.yaml`

Check external ip on ingress controller
`kubectl get services --namespace ingress-nginx`

## Create default PV class
`kubectl create -f pv-class.yaml`

``` yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: local
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
provisioner: kubernetes.io/no-provisioner
volumeBindingMode: WaitForFirstConsumer
```
