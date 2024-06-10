from flask import Flask

app = Flask(__name__)


@app.route("/")
def home_page():
    html = """
    <html>
        <body>
            <h1>Home Page!</h1>
            <p>Welcome to my simple app!</p>
        </body>
    </html>
    """
    return html


@app.route("/welcome")
def welcome():
    return "welcome"


@app.route("/welcome/home")
def welcome_home():
    return "welcome home"


@app.route("/welcome/back")
def welcome_back():
    return "welcome back"
