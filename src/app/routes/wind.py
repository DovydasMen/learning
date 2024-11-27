from app import app

@app.route("/wind")
def wind():
    return "<p> Wind is blowing from other side <p>"