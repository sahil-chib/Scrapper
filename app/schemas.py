from pydantic import BaseModel
from typing import List, Optional

class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    post_id: int

    class Config:
        orm_mode = True

class PostBase(BaseModel):
    title: str 
    link: str
    points: int
    author: str
    time: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    comments: List[Comment] = []

    class Config:
        orm_mode = True
