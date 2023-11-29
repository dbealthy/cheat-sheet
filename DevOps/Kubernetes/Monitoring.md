Add prometheus repository
```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

helm repo update
```

Add loki repository
```
helm repo add loki https://grafana.github.io/helm-charts

helm repo update
```

Create namespace to install plg stack into it
```
kubectl create namespace monitoring
```

Create storage class, persistent volume and persistent volume claim
`pvc.yaml`
``` yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: prometheus-stack #update your helm deployment name accordingly
  labels:
    app.kubernetes.io/name: grafana
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 20Gi #update storage level accordingly
```

```
kubectl create -f pvc.yaml -n monitoring
```


```
helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack -n monitoring
```

Locate grafana service
```
kubectl -n monitoring get svc | grep grafana
```


Configure port forwarding or ingress
```
kubectl -n monitoring port-forward svc/loki-stack-grafana 8080:80
```

Get grafana login and password
```
kubectl -n monitoring get secret | grep grafana
```

```
kubectl -n monitoring get secret/loki-stack-grafana -o custom-columns="VALUE":.data.admin-user --no-headers | base64 --decode
```

```
kubectl -n monitoring get secret/loki-stack-grafana -o custom-columns="VALUE":.data.admin-password --no-headers | base64 --decode
```

admin
prom-operator

Install loki
```
helm install --values loki-values.yaml loki --namespace=monitoring grafana/loki
```

Install promtail
```
helm upgrade --install promtail grafana/promtail --set "loki.serviceName=loki" -n monitoring
```