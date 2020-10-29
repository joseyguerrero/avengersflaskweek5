from flask import Flask

# Import the config Object
from config import Config

# Import forthe SQLAlchemy Object
from flask_sqlalchemy import SQLAlchemy

# Import ehr Migrate Object
from flask_migrate import Migrate

# Import for the Flask Login Module
from flask_login import LoginManager

app = Flask(__name__)
# this completes the config cycle for our Flask App
#And give access to our Database (when we have one)
# along with our Secret Key
app.config.from_object(Config)

# Init our database (db)
db = SQLAlchemy(app)

# Init the migrator
migrate = Migrate(app,db)

# Login Config - Init for the LoginManager
login_manager = LoginManager(app)
login_manager.login_view = 'login' # Specify what page to load for NON-authenticated users

from hmwork2_blog_app import routes,models