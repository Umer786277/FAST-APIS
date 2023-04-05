from fastapi import FastAPI,Depends,status,Response,HTTPException
from . schemas import Item
from. import models
from.import schemas

from.database import engine,SessionLocal
from sqlalchemy.orm import Session


app=FastAPI()

models.Base.metadata.create_all(bind=engine)


def get_db():
    db=SessionLocal()

    try:
        yield db
    finally:
        db.close()







# @app.post('/blog',status_code=status.HTTP_201_CREATED)

# def create(request: Blogs,db:Session=Depends(get_db)):
#     new_blog=models.Blogs(title=request.title,body=request.body)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.delete('/delete/{id}',status_code=status.HTTP_204_NO_CONTENT)

# def destroy(id,db:Session=Depends(get_db)):
#     db.query(models.Blogs).filter(models.Blogs.id==id).delete(synchronize_session=False)
#     db.commit()

#     return 'Blog Deleted!'

# @app.put('/blog/{id}',status_code=status.HTTP_202_ACCEPTED)

# def upadte(id,request:schemas.Blogs,db:Session=Depends(get_db)):
#     db.query(models.Blogs).filter(models.Blogs.id==id).update(request.dict())
#     db.commit()
    
#     return request

# @app.get('/extract')

# def extract(db:Session=Depends(get_db)):
#     all=db.query(models.Blogs).all()
#     return all




# @app.get('/specific/{id}',status_code=200)

# def withid(id, response:Response,db:Session=Depends(get_db)):
#     blog=db.query(models.Blogs).filter(models.Blogs.id==id).first()
#     if not blog:
#         # response.status_code=status.HTTP_404_NOT_FOUND
#         # return {'detail'}
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog is not available with entered ID {id}')
#     return blog


@app.post('/item',status_code=status.HTTP_201_CREATED)

def creates(request:Item,db:Session=Depends(get_db)):
    items=models.Item(name=request.name,about=request.about,price=request.price,man=request.man,exp=request.exp,quantity=request.quantity)
    db.add(items)
    db.commit()
    db.refresh(items)
    return items


@app.get('/item/{id}',status_code=status.HTTP_200_OK)

def fetch(id,response:Response,db:Session=Depends(get_db)):
    blogs=db.query(models.Item).filter(models.Item.id==id).first()
    if not blogs:
        # response.status_code=status.HTTP_404_NOT_FOUND
        # return {'details':f'There is no ITEM avilable with gievn ID {id}'}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'There is no ITEM avilable with gievn ID {id}')
    return blogs


@app.put('/item/{id}',status_code=status.HTTP_202_ACCEPTED)

def upadate(id,request:schemas.Item,db:Session=Depends(get_db)):
    db.query(models.Item).filter(models.Item.id==id).update(request.dict())
    db.commit()
    return request


@app.delete('/item/{id}',status_code=status.HTTP_204_NO_CONTENT)

def destroy(id,db:Session=Depends(get_db)):
    db.query(models.Item).filter(models.Item.id==id).delete(synchronize_session=False)
    db.commit()
    return 'Deleted'