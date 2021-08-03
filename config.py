import os

basedir = os.path.abspath(os.path.dirname(__file__))

#need a secret key to access a page with validation

#after assigning things to class Config, need to import it to init
class Config:
    """
    Sets configuration variable for Flask app
    Eventually will be use hidden variable items
    """
    SECRET_KEY= "In a hole in the ground..."
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    SQLALCHEMY_TRACK_MODIFICATIONS=False