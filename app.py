from flask import Flask,redirect,url_for,render_template,request, flash
import datetime
from models import User, Booking, db
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, login_required, current_user, logout_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)
app.config['SECRET_KEY'] = 'Thisismysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/agrologistics'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///agrologistics.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False

#Database Initiation 
db.init_app(app)
# with app.app_context():
#         db.create_all()

#Flask loging Manager intiation
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'home'

#Track all logging users into the system
@login_manager.user_loader
def load_user(user_id):
   return User.query.get(int(user_id))

#Main entry point to the website
@app.route('/')
def home():
    return render_template('login.html')

#Loging validator 
@app.route("/login", methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(email=username).first()
    #Validate the user before login to the system
    if not user:
        flash("Wrong email or password!!")
        return redirect('/')
    elif username == user.email and check_password_hash(user.password, password):
        if user.account_type == 'Agent':
            login_user(user)
            return redirect(url_for('Agent.dashboard'))
        elif user.account_type == 'Client':
            login_user(user)
            return redirect(url_for('client.clientarea'))
        elif user.account_type == 'Staff':
            login_user(user)
            return redirect(url_for('superadmin.adminpanel'))
        elif user.account_type == 'Driver':
            login_user(user)
            return redirect(url_for('driver.driver_dashboard'))
        #return "Welcome bro!!"
    
    return redirect('/')

#Blueprint for Staff, Agent, client and driver
from Agent import Agent as agent
app.register_blueprint(agent)

from client import client as c
app.register_blueprint(c)

from superadmin import superadmin as sadmin
app.register_blueprint(sadmin)

from driver import driver as dr
app.register_blueprint(dr)

#Logout route
@app.route('/logout')
@login_required 
def logout():
    logout_user()
    return redirect('/')
   
if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    
    app.run(port=5000,debug=True)