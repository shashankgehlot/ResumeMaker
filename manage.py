from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
app.config['SQL_ALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:''@127.0.0.1/PythonApp'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class APP_USER(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(128))
    lastname=db.Column(db.String(128))
    email=db.Column(db.String(128),unique=True)
    phoneno=db.Column(db.Integer(),unique=True)
    picname=db.Column(db.String(20),unique=True)
    description= db.Column(db.Text(), unique=True)

    def __init__(self,firstname,lastname,email,phoneno,picname):
        self.firstname=firstname
        self.lastname= lastname
        self.email=email
        self.phoneno=phoneno
        self.picname=picname

    def __repr__(self):
        return f'User({self.firstname},{self.lastname},{self.email})'

if __name__ == '__main__':
    manager.run()
    # app.run()