from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)  # Specifying length for String
    link = Column(String(255))  # Specifying length for String
    points = Column(Integer)
    author = Column(String(255))  # Specifying length for String
    time = Column(String(255))  # Specifying length for String
    
    comments = relationship('Comment', back_populates='post')

class Comment(Base):
    __tablename__ = 'comments'
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text)
    post_id = Column(Integer, ForeignKey('posts.id'))
    
    post = relationship('Post', back_populates='comments')
