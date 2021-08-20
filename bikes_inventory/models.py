from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import uuid

#add security measures
from werkzeug.security import generate_password_hash, check_password_hash

#create hex token for API access
import secrets

from flask_login import UserMixin, LoginManager
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
# In production, email will have unique=True added after the
# nullable attribute to ensure all emails are unique
login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String, nullable=True)
    token = db.Column(db.String, unique=True)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    bike = db.relationship('Bike', backref='owner', lazy=True)

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

class Bike(db.Model):
    id = db.Column(db.String, primary_key = True)
    model = db.Column(db.String(150))
    manufacturer = db.Column(db.String(150))
    year = db.Column(db.Numeric(precision=4))
    size = db.Column(db.String(25))
    frameMaterial = db.Column(db.String(150), nullable = True)
    category = db.Column(db.String(100), nullable = True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'))

    def __init__(self,model, manufacturer, year, size, frameMaterial, category, user_token, id = ''):
        self.id = self.set_id()
        self.model = model
        self.manufacturer = manufacturer
        self.year = year
        self.size = size
        self.frameMaterial = frameMaterial
        self.category = category
        self.user_token = user_token

    def set_id(self):
        return (secrets.token_urlsafe())

#creating our Marshaller to pull k,v pairs out of Drone instance attributes
class BikeSchema(ma.Schema):
    class Meta:
        # tells which fields to pull out of drone and send to API call
        fields = ['id', 'model', 'manufacturer', 'year', 'size', 'frameMaterial', 'category', 'user_token']
    
bike_schema = BikeSchema()
bikes_schema = BikeSchema(many=True)