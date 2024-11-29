def get_calculated_value(operand: str, value_a: int, value_b: int) -> int:
    """
    Basic calculation is done by summing or deducting values.

    :param operand: desides which math operation to use, provided as string. 
    Optrions is "+" or "-".
    :param value_a: integer value for actual value.
    :param value_b: integer value for actual value.
    
    """
    if operand == "+":
        return value_a + value_b
    elif operand == "-":
        return value_a - value_b
    elif operand == "x" or "*":
        return value_a * value_b
    elif operand == "/":
        return value_a / value_b