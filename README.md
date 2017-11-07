# YAO Bank
(Yet Another Online Bank)

Demo Application for Kubernetes suitable for showing authorization policy.

Consists of 3 microservices:

1. **database** - a single-cluster etcd database.  Stores the state for the demo.
1. **summary** - HTTP service that returns JSON account summaries.
1. **customer** - Front-end web service that displays account summaries to users.

![service graph](https://github.com/spikecurtis/yaobank/raw/master/doc/service-graph.png)

*User icon By MCruz (WMF) (Own work) [CC BY-SA 4.0 (https://creativecommons.org/licenses/by-sa/4.0)], via Wikimedia Commons*

The transaction and teller microservices are microservices that a bank teller would use to process deposits and withdrawals.  They don't feature in the policy demo directly, so have not been built yet.

## How to run

Set up the deployments, service accounts, and services.

```
kubectl apply -f 10-yaobank.yaml
```

*If using Istio*, then run the following to set up the Istio Ingress to the application.

```
kubectl apply -f 20-ingress.yaml
```
