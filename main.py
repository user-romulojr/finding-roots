from flask import Flask, render_template, request
from fr1_bisection import bisection_method
from fr2_fixed_point import fixed_point_method
from fr3_newton_raphson import newton_raphson_method
from fr4_regula_falsi import regula_falsi_method
from fr5_secant import secant_method


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


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
@app.route("/bisection", methods=['POST', 'GET'])
def bisection():
    if request.method == 'POST':
        data = {
            "function" : request.form["function"],
            "minval" : float(request.form["minval"]),
            "maxval" : float(request.form["maxval"]),
            "rerror" : float(request.form["rerror"])
        }
        table = bisection_method(data)
        return render_template("bisection.html", table=table)
    return render_template("bisection.html")

'''
TEST DATA
x ^ 4 - 3x ^ 2 - 3
( 3x^2 + 3) ^ (1/4)
1
0.02
'''
@app.route("/fixed_point", methods=['POST', 'GET'])
def fixed_point():
    if request.method == 'POST':
        data = {
            "function" : request.form["function"],
            "point" : float(request.form["point"]),
            "it-function" : request.form["it-function"],
            "rerror" : float(request.form["rerror"])
        }
        table = fixed_point_method(data)
        return render_template("fixed_point.html", table=table)
    return render_template("fixed_point.html")


'''
TEST DATA
6x + 2lnx - 400
2/x+6
0.025
1
'''
@app.route("/newton_raphson", methods=['POST', 'GET'])
def newton_raphson():
    if request.method == 'POST':
        data = {
            "function" : request.form["function"],
            "point" : float(request.form["point"]),
            "derivative-function" : request.form["derivative-function"],
            "rerror" : float(request.form["rerror"])
        }
        table = newton_raphson_method(data)
        return render_template("newton_raphson.html", table=table)
    return render_template("newton_raphson.html")

'''
TEST DATA
tanx - x - 1
1
1.5
0.02
'''
@app.route("/regula_falsi", methods=['POST', 'GET']) 
def regula_falsi():
    if request.method == 'POST':
        data = {
            "function" : request.form["function"],
            "minval" : float(request.form["minval"]),
            "maxval" : float(request.form["maxval"]),
            "rerror" : float(request.form["rerror"])
        }
        table = regula_falsi_method(data)
        return render_template("regula_falsi.html", table=table)
    return render_template("regula_falsi.html")

'''
TEST DATA
3logx - e ^ (-x)
1
5
1
'''
@app.route("/secant", methods=['POST', 'GET'])
def secant():
    if request.method == 'POST':
        data = {
            "function" : request.form["function"],
            "minval" : float(request.form["minval"]),
            "maxval" : float(request.form["maxval"]),
            "rerror" : float(request.form["rerror"])
        }
        table = secant_method(data)
        return render_template("secant.html", table=table)
    return render_template("secant.html")

if __name__ == '__main__':
    app.run(debug=True, port=8000)
