from flask import Flask, render_template, request
from bisection import bisection

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("app.html")

@app.route("/query", methods=["POST"])
def query():
    data = {
        "function" : request.form["function"],
        "minval" : request.form["minval"],
        "maxval" : request.form["maxval"],
        "rerror" : request.form["rerror"]
    }

    table = bisection(data)

    return render_template("app.html", **data, table=table)

if __name__ == '__main__':
    app.run(debug=True, port=8000)

#cchange
# hello