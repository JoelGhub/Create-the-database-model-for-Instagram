import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er
import enum

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

    post_id = relationship('Post', backref='user', lazy=True)
    comment_id = relationship('Comment', backref='user', lazy=True)
    follower_from_id = relationship('Follower', backref='user', lazy=True)
    follower_to_id = relationship('Follower', backref='user', lazy=True)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    
    post_id = relationship('Comment', backref='post', lazy=True)
    media_id = relationship('Media', backref='post', lazy=True)

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    post_id = Column(Integer,ForeignKey('post.id'))
    user_id = Column(Integer,ForeignKey('user.id'))
    
    
    

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type_ = Column(String(100), nullable=False)
    url = Column(String(100), nullable=False)
    post_id = Column(Integer,ForeignKey('post.id'))


class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    user_from_id = Column(Integer,ForeignKey('user.id'),primary_key=True)
    user_to_id = Column(Integer,ForeignKey('user.id'),primary_key=True)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e