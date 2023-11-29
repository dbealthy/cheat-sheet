Docs: https://kubernetes.github.io/ingress-nginx/deploy/

1. Install helm on local PC 
   `sudo dnf install helm`
2. Add ingress repo 
   `helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx`
3. Find appropriate version
   `helm search repo ingress-nginx --versions`