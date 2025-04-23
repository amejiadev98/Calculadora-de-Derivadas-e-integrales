from flask import Flask, render_template, request
from sympy import symbols, diff, integrate, sympify

app = Flask(__name__)
x = symbols('x')

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        function = request.form["function"]
        operation = request.form["operation"]
        try:
            expr = sympify(function)
            if operation == "derivar":
                result = diff(expr, x)
            elif operation == "integrar":
                result = integrate(expr, x)
        except Exception as e:
            result = f"Error: {e}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
