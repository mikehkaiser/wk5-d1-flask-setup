from flask import Flask
from config import Config
from .site.routes import site
#import authentication.routes, variable auth
from .authentication.routes import auth
from flask_migrate import Migrate
from .models import db

app = Flask(__name__)

app.register_blueprint(site)

#register blueprint for signin and signup as 'auth'
app.register_blueprint(auth)

#register config with app so it can do something with it
app.config.from_object(Config)

db.init_app(app)

migrate = Migrate(app, db)

from .models import User