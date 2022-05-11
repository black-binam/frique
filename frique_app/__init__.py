from flask import Flask
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config['SECRET_KEY'] ="8138ba524d152a5c110035a482f96acf"
db = SQLAlchemy(app)


from frique_app import routes

