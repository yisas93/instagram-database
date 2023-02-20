import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

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

class Follower(Base):
    __tablename__= "follower"
    id = Column(Integer, primary_key=True)
    user_from_id=Column(Integer, ForeignKey('user.id'))
    user_from_user=relationship(User)
    user_to_id=Column(Integer, ForeignKey('user.id'))
    user_to_user=relationship(User)
class Post(Base):
    __tablename__="post"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_to_user= relationship(User)
class Comment(Base):
    __tablename__="comment"
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'))
    author_to_post = relationship(User)
    post_id= Column(Integer, ForeignKey('post.id'))
    comment_to_post= relationship(Post)



class Media (Base):
    __tablename__="media"
    id=Column(Integer, primary_key=True)
    url= Column(String(250), nullable=False)
    post_id= Column(Integer, ForeignKey('post.id'))
    to_post_id=relationship(Post)


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
