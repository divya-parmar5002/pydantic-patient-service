from pydantic import BaseModel
class Address(BaseModel):
    city:str
    state:str
    pin:str
    country:str
    