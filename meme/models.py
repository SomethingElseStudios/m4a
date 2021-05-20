from sqlalchemy.engine import url
from app import db
from uuid import uuid4
# from flask_login import UserMixin
# from sqlalchemy.sql import func

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime(timezone=True))
    
    def __init__(self, username, email, password):
        self.name = username
        self.email = email
        self.password = password
class Posts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    postName = db.Column(db.String(100))
    url = db.Column(db.String(100))

    def __init__(self, url, postname) -> None:
        self.url = url
        self.postName = postname




def addPost(name, url) -> Posts:
    post = Posts(url, name)
    db.session.add(post)
    db.session.commit()
    return post

def addUser(username, email, password) -> User:
    newUser = User(username, email, password)
    db.session.add(newUser)
    db.session.commit()
    return newUser
# import models

if __name__ == "__main__":
    print("creating the database")
    db.create_all()