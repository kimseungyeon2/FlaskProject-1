from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'User'
    id = Column(db.Integer, primary_key=True)
    username = Column(db.String(80), nullable=False, unique=True)
    password = Column(db.String(80))
    sessionId  = Column(db.String(120), unique=True)
    # constructor
    def __init__(self,username,password):
        self.username = username
        self.password = password

