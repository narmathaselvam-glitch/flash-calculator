
from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Calculator</title>
</head>
<body>
    <h2>Flask Calculator</h2>

    <form method="POST">
        <input type="number" step="any" name="num1"
               placeholder="First number" required>

        <select name="operation">
            <option value="add">Addition (+)</option>
            <option value="sub">Subtraction (-)</option>
            <option value="mul">Multiplication (*)</option>
            <option value="div">Division (/)</option>
        </select>

        <input type="number" step="any" name="num2"
               placeholder="Second number" required>

        <button type="submit">Calculate</button>
    </form>

    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def calculator():
    result = None

    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]

        if operation == "add":
            result = num1 + num2
        elif operation == "sub":
            result = num1 - num2
        elif operation == "mul":
            result = num1 * num2
        elif operation == "div":
            if num2 == 0:
                result = "Cannot divide by zero"
            else:
                result = num1 / num2

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5003, debug=False)
