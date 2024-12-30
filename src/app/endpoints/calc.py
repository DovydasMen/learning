from app import app

from app.backend.calculator import get_calculated_value
from app.pydantic_validation_models.calculator_validator import CalcValidator
from pydantic import ValidationError
from flask import request

@app.route("/calc", methods=['GET'])
def calc():
    try:
        print(request.args.get("operand"))
        calc_query_results = CalcValidator(
            value_a=request.args.get("value_a", type=int),
            value_b=request.args.get("value_b", type=int),
            operand=request.args.get("operand", type=str))
        
        print(calc_query_results.operand)
        print(type(calc_query_results.operand))
        
        calc_result = get_calculated_value(
            operand=calc_query_results.operand,
            value_a=calc_query_results.value_a,
            value_b=calc_query_results.value_b)

        return f"Result = {calc_result}"

    except ValidationError as e:
        return f"We reciewed wrong type on information, validation haven't \
                passed."
    
    except Exception as e:
        return f"Something went wrong."
    