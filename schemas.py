from pydantic import BaseModel

class Item(BaseModel):
    name:str
    price:float
    man:float
    exp:float
   
    quantity:float