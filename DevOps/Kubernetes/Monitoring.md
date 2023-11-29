```
helm repo add grafana https://grafana.github.io/helm-charts
```

Create config
```
prometheus:
  enabled: true
  isDefault: false
  url: http://{{ include "prometheus.fullname" .}}:{{ .Values.prometheus.server.service.servicePort }}{{ .Values.prometheus.server.prefixURL }}
  datasource:
    jsonData: "{}"

loki:
  enabled: true
  isDefault: true
  url: http://{{(include "loki.serviceName" .)}}:{{ .Values.loki.service.port }}
  readinessProbe:
    httpGet:
      path: /ready
      port: http-metrics
    initialDelaySeconds: 45
  livenessProbe:
    httpGet:
      path: /ready
      port: http-metrics
    initialDelaySeconds: 45
  datasource:
    jsonData: "{}"
    uid: ""

promtail:
  enabled: true
  config:
    logLevel: info
    serverPort: 3101
    clients:
      - url: http://{{ .Release.Name }}:3100/loki/api/v1/push

grafana:
  enabled: true 
  sidecar:
    datasources:
      label: ""
      labelValue: ""
      enabled: true
      maxLines: 1000
  image:
    tag: 10.0.2
```


Create namespace and install plg stack into it
```
kubectl create namespace monitoring
```

```
helm install -n monitoring --values values.yaml loki-stack grafana/loki-stack
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