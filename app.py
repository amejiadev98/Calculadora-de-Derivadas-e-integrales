def index():
    result = ""
    if request.method == "POST":
        function = request.form["function"]
        operation = request.form["operation"]
        order = int(request.form.get("order", 1))  # Para derivadas de orden superior
        lower_limit = request.form.get("lower_limit")
        upper_limit = request.form.get("upper_limit")
        
        try:
            expr = sympify(function)
            if operation == "derivar":
                result = diff(expr, x, order)
            elif operation == "integrar":
                result = integrate(expr, x)
            elif operation == "integrar_definida":
                if lower_limit and upper_limit:
                    result = integrate(expr, (x, float(lower_limit), float(upper_limit)))
                else:
                    result = "Debe ingresar los límites inferior y superior."
            elif operation == "simplificar":
                result = simplify(expr)
        except Exception as e:
            result = f"Error: {e}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
