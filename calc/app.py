from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route("/")
def index():
    return """
      <html>
        <body>
          <h1>HI! I am the landing page</h1>
        </body>
      </html>
      """


@app.route("/<op>")
def operation_route(op):
    a = int(request.args["a"])
    b = int(request.args["b"])
    if op == "add":
        result = str(add(a, b))
    elif op == "sub":
        result = str(sub(a, b))
    elif op == "mult":
        result = str(mult(a, b))
    elif op == "div":
        result = str(div(a, b))
    else:
        result = "INVLID OPERATION"
    return result


@app.route("/math/<op>")
def math_opeartion_route(op):
    ops = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
    }

    a = int(request.args["a"])
    b = int(request.args["b"])

    if op in ops:
        result = str(ops[op](a, b))

    return result
