from flask import Flask, jsonify
import etcd

app = Flask(__name__)

@app.route("/<userid>")
def get_summary(userid):
    client = etcd.Client(host="database", port=2379)
    summary = {}
    key = "/accounts/%s" % userid
    result = client.read(key, recursive=True)
    for child in result.children:
        subkey = child.key[len(key)+1:]
        summary[subkey] = child.value
    return jsonify(summary)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)