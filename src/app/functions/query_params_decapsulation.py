from typing import Dict, Optional
from flask import request

def get_wind_side() -> Optional[str]:
    return request.args.get("wind_side")

def get_calc_values_operand() -> Optional[Dict[str, str]]:
    calc_values = {}
    if request.args.get("value_a") \
        and request.args.get("value_b") \
            and request.args.get("operand") \
                != None:
        calc_values["value_a"] = request.args.get("value_a")
        calc_values["value_b"] = request.args.get("value_b")
        calc_values["operand"] = request.args.get("operand")
        return calc_values