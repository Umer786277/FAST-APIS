from pydantic import BaseModel

# class Blogs(BaseModel):
#     title:str
#     body:str


class Item(BaseModel):
    name:str
    about:str
    price:int
    man:str
    exp:str
   
    quantity:int