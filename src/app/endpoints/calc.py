from app import app

from app.functions.query_params_decapsulation import get_calc_values_operand
from app.backend.calculator import get_calculated_value

@app.route("/calc")
def calc():
    query_result = get_calc_values_operand()
    if query_result:
        calc_result = get_calculated_value(operand=query_result["operand"],
                                       value_a=int(query_result["value_a"]),
                                       value_b=int(query_result["value_b"]))
        return f"Result = {calc_result}"
    else:
        return "Calculator is not working, no query params was set."