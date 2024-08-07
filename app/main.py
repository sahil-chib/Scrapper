from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from . import crud, models, scrape

app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/scrape")
def scrape_data(db: Session = Depends(get_db)):
    try:
        scrape.scrape_ycombinator(db)
        return {"status": "Scraping completed"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/data")
def read_data(skip: int = 0, limit: int = 30, db: Session = Depends(get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return posts


@app.get("/status")
def read_status():
    return {"status": "Scraping service is up and running"}
