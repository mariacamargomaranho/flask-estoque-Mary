from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from flask_minify import Minify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_login import LoginManager

class Base(DeclarativeBase):
    pass

bootstrap = Bootstrap5()
minify = Minify()
db = SQLAlchemy(model_class=Base,
                disable_autonaming=True)
login = LoginManager()