1. Install kubectl from official docs https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
2. Make ~/.kube directory
   `mkdir ~/.kube`
3. Copy kube config to ~/.kube directory
   `scp user@185.146.1.232:/home/user/.kube/config ~/.kube`
4. Check configuration
   `kubectl config view`
5. Set cluster and pass its ip address
``` bash
kubectl config set-cluster kubernetes --server=https://185.146.1.232:6443
```