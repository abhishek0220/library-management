from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
import os

app = Flask(__name__)

api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['MSSQLSTRING']
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_SECRET_KEY'] = 'thisisjwtsecretkey'
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
db.create_all()

jwt = JWTManager(app)


@app.route('/')
def hdfd():
    return f"Running..."

from Library.Resources import admin
api.add_resource(admin.Publisher, '/publisher')
api.add_resource(admin.Rental, '/rental')
api.add_resource(admin.Reader, '/reader')
api.add_resource(admin.Login, '/login')
api.add_resource(admin.TestClass, '/test')
