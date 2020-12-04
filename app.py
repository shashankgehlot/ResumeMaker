from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from werkzeug.utils import secure_filename
import os
app=Flask(__name__,static_url_path = '/static')
app.config['UPLOAD_FOLDER'] = './static/styles/images/'
app.config['SECRET_KEY']='abc'
app.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://root:''@127.0.0.1/PythonApp'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

class APP_USER(db.Model):
   id = db.Column(db.Integer, primary_key=True,autoincrement=True)
   firstname = db.Column(db.String(128))
   lastname = db.Column(db.String(128))
   username= db.Column(db.String(128),unique=True)
   email = db.Column(db.String(128), unique=True)
   phoneno = db.Column(db.Integer(), unique=True)
   discription = db.Column(db.Text())
   picname = db.Column(db.String(20), unique=True)

   def __init__(self, firstname, lastname, email, phoneno,discription,picname,username):
      self.firstname = firstname
      self.lastname = lastname
      self.username=username
      self.email = email
      self.phoneno = phoneno
      self.discription=discription
      self.picname=picname


   def __repr__(self):
      return f'User({self.firstname},{self.lastname})'


@app.route('/')
def hello_world():
   return render_template('Resume_view.html')

@app.route('/add_resume')
def add_resume():
   return render_template('Resume_Form.html')

@app.route('/form_submission',methods=["POST"])
def form_submission():
   if request.method=='POST':
      if 'file' in request.files:
         file = request.files['file']
         filename = secure_filename(file.filename)
         file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      data=APP_USER(firstname=request.form['fname'],lastname= request.form['lname'],username=request.form['username'],
            phoneno=request.form['phoneno'], email=request.form['email'],discription=request.form['description'],
            picname=filename)
      print(data)
      db.session.add(data)
      db.session.commit()
      return "success"


if __name__ == '__main__':
   #app.run(debug=True)
   manager.run()


