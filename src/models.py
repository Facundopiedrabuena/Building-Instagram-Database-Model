import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Username = Column(String(250), nullable=False)
    Firstname = Column(String(250), nullable=False)
    Lastname = Column(String(250), nullable=False)
    Email = Column(String(250), nullable=False)

class Followers(Base):
    __tablename__ = 'Followers'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    User_from_id = Column (Integer, ForeignKey('User.id'), primary_key = True, nullable=False)
    User_to_id = Column (Integer, ForeignKey('User.id'), primary_key = True, nullable=False)
    


class Post(Base):
    __tablename__ = 'Post'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    User_id = Column (Integer, ForeignKey('User.id'), primary_key = True, nullable=False)

class Media(Base):
    __tablename__ = 'Media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    type = Column (String(250), nullable=False)
    url = Column (String(250), nullable=False)
    post_ID = Column (Integer, ForeignKey('Post.id'))

class Comment(Base):
    __tablename__ = 'Comment'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    Coment_text = Column (String(250), nullable=False)
    author_ID = Column (Integer, ForeignKey('User.id'))
    post_ID = Column (Integer, ForeignKey('Post.id'))

    
    





    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e