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
        "minval" : float(request.form["minval"]),
        "maxval" : float(request.form["maxval"]),
        "rerror" : float(request.form["rerror"])
    }

    table = bisection(data)

    '''
    TEST DATA #1:
    1.75
    3.25
    0.02
    x^3 - 0.73x^2 - 44.0085x + 100.387125

    TEST DATA #2:
    -5
    -3.5
    0.02
    cosx - xe^x
    '''

    return render_template("app.html", **data, table=table)

if __name__ == '__main__':
    app.run(debug=True, port=8000)
