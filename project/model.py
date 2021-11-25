
from project import db, bcrypt, login_manager


class User(db.Model):
    ID = db.Column(db.Integer,Primary_Key = True )
    firstName= db.Column(db.String(20))
    LastName= db.Column(db.String(20))
    firstLoginTime = db.Column(db.DateTime)
    lastLoginTime = db.Column(db.DateTime)
