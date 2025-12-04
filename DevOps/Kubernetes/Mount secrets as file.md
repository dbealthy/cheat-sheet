https://itnext.io/how-to-mount-secrets-as-files-or-environment-variables-in-kubernetes-f03d545dcd89


``` yaml
apiVersion: apps/v1  
kind: Deployment  
metadata:  
  labels:  
    app: example  
  name: example  
  namespace: example  
spec:  
  replicas: 1  
  selector:  
    matchLabels:  
      app: example  
  template:  
    metadata:  
      labels:  
        app: example  
    spec:  
      containers:  
      - name: example  
        image: busybox:1.36  
        command: ["sh", "-c", "/bin/sleep 3600"]  
        volumeMounts:  
          - mountPath: "/var/mysecrets"  
            name: test.json  
            readOnly: true  
      volumes:  
        - name: test.json  
          secret:  
            secretName: supersecret2
```


Или для одного файла

``` yaml
apiVersion: apps/v1  
kind: Deployment  
metadata:  
  labels:  
    app: example  
  name: example  
  namespace: example  
spec:  
  replicas: 1  
  selector:  
    matchLabels:  
      app: example  
  template:  
    metadata:  
      labels:  
        app: example  
    spec:  
      containers:  
      - name: example  
        image: busybox:1.36  
        command: ["sh", "-c", "/bin/sleep 3600"]  
        volumeMounts:  
          - mountPath: "/var/myapp/server.config"  
            name: config  
            readOnly: true  
            subPath: test.json  
      volumes:  
        - name: config  
          secret:  
            secretName: supersecret2  
            items:  
              - key: test.json  
                path: test.json
```