1. Authenticate to registry
   `docker login gitlab.imas.kz:5050`
2. Run command to kuberentes to add image registry
``` bash
kubectl create secret docker-registry regcred --docker-server=<your-registry-server> --docker-username=<your-name> --docker-password=<your-pword> --docker-email=<your-email>
```
3. Each manifest file will contain name of that secret
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: private-reg
spec:
  containers:
  - name: private-reg-container
    image: <your-private-image>
  imagePullSecrets:
  - name: regcred
```

This part is important:
imagePullSecrets:
  - name: regcred 