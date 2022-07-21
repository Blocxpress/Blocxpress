#Run pip install flask-blueprint
<<<<<<< HEAD
from flask import Blueprint, render_template, request, redirect
=======
from flask import Blueprint, render_template, request, redirect, url_for
>>>>>>> f12ca09740b6138758e806c7fdd090e65fc4447a
from models import Booking, User, db
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, login_required, current_user, logout_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

Agent = Blueprint('Agent',__name__)

#Agent registration form
@Agent.route('/register')
def register():
    return render_template('register.html')

#process Agent registration 
@Agent.route('/process', methods=['POST'])
def process():
    fname = request.form.get('firstname')
    lname = request.form.get('lastname')
    email_id = request.form.get('email')
    password_id = request.form.get('password')
    account_type = request.form.get('account_type')

    users = User.query.filter_by(email=email_id).first()
    if users:
        return redirect(url_for('Agent.register'))
    register_date = datetime.datetime.utcnow()
    new_user =User(firstname=fname, lastname=lname, email=email_id, password=generate_password_hash(password_id,method='sha256'), account_type=account_type, register_date=register_date)
    db.session.add(new_user)
    db.session.commit()
    return render_template('confirmation.html', firstname=fname)

#Load the Agent dashboard 
@Agent.route("/dashboard")
@login_required
def dashboard():
    getRequest = Booking.query.all()
    return render_template('dashboard.html', firstname=current_user.firstname, lastname=current_user.lastname, getRequest=getRequest)

#Agent profile 
@Agent.route('/agentprofile')
@login_required
def agentprofile():
    users_profit = User.query.filter_by(id=current_user.id).first()
    update_agent_profile = [users_profit]
    return render_template('agentprofile.html', firstname=current_user.firstname, lastname=current_user.lastname, update_agent_profile=update_agent_profile)

#view client request
@Agent.route('/client_request')
@login_required
def client_request():
    return render_template('agent_view_req.html', firstname=current_user.firstname, lastname=current_user.lastname)

#Add driver 
@Agent.route('/add_driver')
@login_required
def add_driver():
    return render_template('adddriver.html', firstname=current_user.firstname, lastname=current_user.lastname)

#view client request
@Agent.route('/agenttrans')
@login_required
def agenttrans():
    return render_template('agenttrans.html', firstname=current_user.firstname, lastname=current_user.lastname)

# View registered drivers
@Agent.route('/viewdrivers')
@login_required
def viewdrivers():
    return render_template('viewdrivers.html', firstname=current_user.firstname, lastname=current_user.lastname)

#Agent support 
@Agent.route('/support_agent')
@login_required
def support_agent():
    return "coming soon "