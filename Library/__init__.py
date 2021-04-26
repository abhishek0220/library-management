from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
import os

app = Flask(__name__)

api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['MSSQLSTRING']
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()


@app.route('/')
def hdfd():
    return f"Running..."

from Library.Resources import admin
api.add_resource(admin.Publisher, '/publisher')
api.add_resource(admin.Rental, '/rental')
api.add_resource(admin.Reader, '/reader')
