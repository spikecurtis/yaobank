from flask import Flask, render_template
import requests

app = Flask(__name__)
userid = "519940"

@app.route("/")
def home():
	r = requests.get("http://summary/%s" % userid)
	summary = r.json()

	return render_template("accountsummary.html", **summary)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)