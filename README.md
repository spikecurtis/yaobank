# YAO Bank
(Yet Another Online Bank)

Demo Application for Kubernetes suitable for showing authorization policy.

Consists of 3 microservices:

1. **database** - a single-cluster etcd database.  Stores the state for the demo.
1. **summary** - HTTP service that returns JSON account summaries.
1. **customer** - Front-end web service that displays account summaries to users.


## How to run

```
kubectl apply -f 10-yaobank.yaml
```

Sets up the deployments, service accounts, and services.

```
kubectl apply -f 20-loaddata.yaml
```

Pushes initial data into the database using a Kubernetes Job.

*If using Istio*, then run the following to set up the Istio Ingress to the application.

```
kubectl apply -f 30-ingress.yaml
```
