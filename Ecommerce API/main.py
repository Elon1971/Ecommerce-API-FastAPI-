from database import SessionLocal, engine
from fastapi import FastAPI, Response, status
from fastapi import Depends, HTTPException
import models
import schemas
from sqlalchemy.orm import Session


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Ecommerce API", description="Ecommerce API")

# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Sources
@app.get("/sources/", tags=["sources"], response_model=list[schemas.API])
def get_data(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    data = db.query(models.API).offset(skip).limit(limit).all()
    return data


@app.get("/sources/{pk}", tags=["sources"], response_model=schemas.API)
def get_data_by_id(pk: int, db: Session = Depends(get_db)):
    data = db.query(models.API).filter(models.API.id == pk).first()
    if data is None:
        raise HTTPException(status_code=404, detail="User not found")
    return data

# Categories
@app.get("/categories/", tags=["Categories"], response_model=list[schemas.API])
def get_data(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    data = db.query(models.API).offset(skip).limit(limit).all()
    return data


@app.get("/categories/{pk}", tags=["Categories"], response_model=schemas.API)
def get_data_by_id(pk: int, db: Session = Depends(get_db)):
    data = db.query(models.API).filter(models.API.id == pk).first()
    if data is None:
        raise HTTPException(status_code=404, detail="User not found")
    return data


@app.put("/categories/{pk}", tags=["Categories"], response_model=schemas.API)
def update_data(pk: int, item: schemas.API, db: Session = Depends(get_db)):
    fd = db.query(models.API).filter(models.API.id == pk)
    fd.update(item.dict())
    db.commit()
    return fd.first()

# Products
@app.get("/products/", tags=["products"], response_model=list[schemas.API])
def get_data(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    data = db.query(models.API).offset(skip).limit(limit).all()
    return data


@app.get("/products/{pk}", tags=["products"], response_model=schemas.API)
def get_data_by_id(pk: int, db: Session = Depends(get_db)):
    data = db.query(models.API).filter(models.API.id == pk).first()
    if data is None:
        raise HTTPException(status_code=404, detail="User not found")
    return data

# Tasks
@app.get("/tasks/state/{task_id}", tags=["tasks"], response_model=schemas.API)
def get_data_by_id(task_id: int, db: Session = Depends(get_db)):
    data = db.query(models.API).filter(models.API.id == task_id).first()
    if data is None:
        raise HTTPException(status_code=404, detail="User not found")
    return data

# Scrapes
@app.get("/scrapes/", tags=["scrapes"], response_model=list[schemas.API])
def get_data(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    data = db.query(models.API).offset(skip).limit(limit).all()
    return data


@app.post("/scrapes/bulk-start/", tags=["scrapes"],  response_model=schemas.API)
def create_data(item: schemas.API, db: Session = Depends(get_db)):
    db_item = models.API(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.post("/scrapes/categories/start", tags=["scrapes"], response_model=schemas.API)
def create_data(item: schemas.API, db: Session = Depends(get_db)):
    db_item = models.API(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.get("/scrapes/{pk}", tags=["scrapes"], response_model=schemas.API)
def get_data_by_id(pk: int, db: Session = Depends(get_db)):
    data = db.query(models.API).filter(models.API.id == pk).first()
    if data is None:
        raise HTTPException(status_code=404, detail="User not found")
    return data


@app.post("/scrapes/{pk}/start", tags=["scrapes"], response_model=schemas.API)
def create_data(item: schemas.API, db: Session = Depends(get_db)):
    db_item = models.API(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


@app.post("/scrapes/{pk}/stop", tags=["scrapes"], response_model=schemas.API)
def create_data(item: schemas.API, db: Session = Depends(get_db)):
    db_item = models.API(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Tests
@app.get("/tests/", tags=["tests"], response_model=list[schemas.API])
def get_data(skip: int = 0, limit: int = 1000, db: Session = Depends(get_db)):
    data = db.query(models.API).offset(skip).limit(limit).all()
    return data


