
from project import db, bcrypt, login_manager
# from flask import current_app
# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship



class User(db.Model):
    __tablename__ = "User" 
    id = db.Column(db.Integer, primary_key=True)
    firstName= db.Column(db.String(20))
    LastName= db.Column(db.String(20))
    firstLoginTime = db.Column(db.DateTime)
    lastLoginTime = db.Column(db.DateTime)
