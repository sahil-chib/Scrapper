from sqlalchemy.orm import Session
from .models import Post, Comment

def get_posts(db: Session, skip: int = 0, limit: int = 30):
    return db.query(Post).offset(skip).limit(limit).all()

def get_post_comments(db: Session, post_id: int):
    return db.query(Comment).filter(Comment.post_id == post_id).all()
