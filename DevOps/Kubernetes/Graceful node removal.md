List the nodes and get the `<node-name>` you want to drain or (remove from cluster)

```yaml
kubectl get nodes
```

1) First drain the node

```yaml
kubectl drain <node-name>
```

You might have to ignore daemonsets and local-data in the machine

```yaml
kubectl drain <node-name> --ignore-daemonsets --delete-local-data
```

2) Edit instance group for nodes (Only if you are using kops)

```yaml
kops edit ig nodes
```

Set the MIN and MAX size to whatever it is -1 Just save the file (nothing extra to be done)

You still might see some pods in the drained node that are related to daemonsets like networking plugin, fluentd for logs, kubedns/coredns etc

3) Finally delete the node

```yaml
kubectl delete node <node-name>
```

4) Commit the state for KOPS in s3: (Only if you are using kops)

```yaml
kops update cluster --yes
```

OR (if you are using kubeadm)

**On node machine**:
If you are using kubeadm and would like to reset the machine to a state which was there before running `kubeadm join` then run

```yaml
kubeadm reset
```