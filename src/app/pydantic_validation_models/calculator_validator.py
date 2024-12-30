from pydantic import BaseModel, Field

class CalcValidator(BaseModel):
    value_a : int = Field(..., ge=0)
    value_b: int = Field(..., ge=0)
    operand: str = Field(...)