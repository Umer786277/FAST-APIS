from.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

# class Blogs(Base):
#     __tablename__='blog'
#     id=Column(Integer,primary_key=True,index=True)
#     title=Column(String)
#     body=Column(String)

# from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class Item(Base):
    __tablename__='item'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String) 
    about=Column(String)
    price=Column(Integer)
    exp=Column(String)
    man=Column(String)
    quantity=Column(Integer)