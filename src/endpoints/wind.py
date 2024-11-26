from app import app

@app.route("/vejas")
def wind():
    return "<p> Wind is blowing from other side <p>"