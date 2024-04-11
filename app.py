import random
from datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Witaj użytkowniku!"


@app.route("/hello/<username>")
def name(username):
    return username


@app.route("/time")
def get_date():
    return str(datetime.date(datetime.now()))


@app.route("/licz/<int:a>/<int:b>")
def add_numbers(a, b):
    return str(a + b)


@app.route("/losuj")
def random_number():
    random_numbers = [str(random.randint(0, 9)) for _ in range(3)]
    return ', '.join(random_numbers)


# @app.route("/lotek")
# def lotto():
#     digits = list(range(1, 50))
#     shuffle(digits)
#     return "-".join(str(d) for d in digits[:6])


# @app.route("/lotek")
# def lotto():
#     digits = []
#
#     while len(digits) <= 6:
#         digit = str(random.randint(1, 49))
#         if digit not in digits:
#             digits.append(digit)
#
#     return '-'.join(digits)


@app.route("/kontakt", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        first_name = request.form.get("firstName")
        return render_template("conformation.html", first_name=first_name)
    return render_template("form.html")


operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


@app.route('/calc', methods=['GET', 'POST'])
def calculator():
    result = ''
    if request.method == 'POST':
        operation = request.form.get("operation")

        try:
            digit1 = float(request.form.get("digit1"))
            digit2 = float(request.form.get("digit2"))

        except ValueError:
            return render_template("calculator.html", result=result, message="Podaj poprawne liczby!")

        operations.get(operation)(digit1, digit2)

    return render_template('calculator.html')


@app.route('/method', methods=['GET', 'POST'])
def check_method():
    if request.method == 'POST':
        return 'Wysłałeś POST'
    return 'Wysłałeś GET'
