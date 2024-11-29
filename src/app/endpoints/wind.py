from app import app
from app.functions.query_params_decapsulation import get_wind_side

@app.route("/wind")
def wind():
    return f"<p> Wind is blowing from {get_wind_side()} <p>"