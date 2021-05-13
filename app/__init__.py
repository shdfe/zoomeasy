from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import os
import flask_migrate
from .util import get_closest

app = Flask(__name__)

#bootstrap = Bootstrap(app)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['BOOTSTRAP_BOOTSWATCH_THEME'] = 'Flatly'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') or 'xxxxxxxxxxxxxxxxxxxxxxxxxxx'
db = SQLAlchemy(app)
app.config['JSON_SORT_KEYS'] = False
bootstrap = Bootstrap(app)
migrate = flask_migrate.Migrate(app, db)
db.create_all()

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Zoom=Zoom, get_closest=get_closest)
from app import routes
from app.models import Zoom
