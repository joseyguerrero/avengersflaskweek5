# Import the os module
import os

# creation of base directory for application
basedir = os.path.abspath(os.path.dirname(__file__))

#windows = Documents\chicodes_sept2020\week_5\in_class
#mac & linux = Documents/chicodes_sept2020/week_5/in_class


# Config Class
# Configure the database (when we have one) and configure
# the secret key for the encription of our submitted forms
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess this...'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False