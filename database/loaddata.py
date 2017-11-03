import etcd

client = etcd.Client(host="database", port=2379)
with open("data.txt") as datafile:
    for line in datafile:
        key, value = line.split(" ", 1)
        client.set(key, value.strip())

