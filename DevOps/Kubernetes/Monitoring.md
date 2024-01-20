# Installation

  

## Preparation

  

### Create persistent volumes of local type or any other type to be used by pvc

- prometheus-storage (10Gi)

- alertmanager-storage (3Gi)

- grafana-storage (2Gi)

  

PVs are defined in [prometheus-pv.yaml](prometheus-pv.yaml) file

### Add prometheus repository

```

helm repo add prometheus-community https://prometheus-community.github.io/helm-charts

```

### Add loki repository

```

helm repo add loki https://grafana.github.io/helm-charts

```

### Update helm repo

```

helm repo update

```

### Create namespace

```

kubectl create namespace monitoring

```

## Prometheus + Grafana + Alertmanager

### Install prometheus with [values](prometheus-values.yaml)

```

helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack --values prometheus-values.yaml -n monitoring

```
### Locate grafana service

```

kubectl -n monitoring get svc | grep grafana

```

### Configure port forwarding (for testing) or ingress (for prod)

```

kubectl -n monitoring port-forward svc/loki-stack-grafana 8080:80

```

  

### Get grafana login and password

```

kubectl -n monitoring get secret | grep grafana

```

```

kubectl -n monitoring get secret/loki-stack-grafana -o custom-columns="VALUE":.data.admin-user --no-headers | base64 --decode

```

```

kubectl -n monitoring get secret/loki-stack-grafana -o custom-columns="VALUE":.data.admin-password --no-headers | base64 --decode

```

> Default admin name and password are located in values file

  

## Loki + Promtail

### Install loki with [values](loki-values.yaml)

```

helm install --values loki-values.yaml loki --namespace=monitoring grafana/loki

```
### Install promtail

```

helm upgrade --install promtail grafana/promtail --set "loki.serviceName=loki" -n monitoring

```