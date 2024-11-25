from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello World! <p>"

@app.route("/vejas")
def wind():
    return "<p> Wind is blowing from other side <p>"


if __name__ == "__main__":
    app.run(port=7000)