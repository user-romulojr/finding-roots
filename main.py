from flask import Flask, render_template, request
from fr1_bisection import bisection_method
'''
from fr2_fixed_point import fixedpoint
from fr3_newton_raphson import newton_raphson
from fr4_regula_falsi import regula_falsi
from fr5_secant import secant
'''

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("app.html")


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
        print("truee")
        data = {
            "function" : request.form["function"],
            "minval" : float(request.form["minval"]),
            "maxval" : float(request.form["maxval"]),
            "rerror" : float(request.form["rerror"])
        }
        table = bisection_method(data)
        return render_template("bisection.html", table=table)
    return render_template("bisection.html")

@app.route("/fixed-point")
def fixed_point():
    return render_template("fixed_point.html")

@app.route("/newton-raphson")
def newton_raphson():
    return render_template("newton_raphson")

@app.route("/regula-falsi") 
def regula_falsi():
    return render_template("regula_falsi")

@app.route("/secant")
def secant():
    return render_template("secant")


if __name__ == '__main__':
    app.run(debug=True, port=8000)
