from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import uuid

#add security measures
from werkzeug.security import generate_password_hash

#create hex token for API access
import secrets

db = SQLAlchemy()

# In production, email will have unique=True added after the
# nullable attribute to ensure all emails are unique

class User(db.Model):
    id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    password = db.Column(db.String, nullable=True)
    token = db.Column(db.String, unique=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, email, password, id='', token=''): 
        self.id = self.set_id()
        self.email = email
        self.password = self.set_password(password) 
        self.token = self.set_token(24)

    def set_id(self):
        return str(uuid.uuid4())

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def set_token(self, length):
        return secrets.token_hex(length)

# set_id creates a unique id without any user input
# set_password takes in the user-added password, hashes it, and stores
# the hashed value as the password in the db
# set_token makes a unique 24-bit token (length=24) and stores that 