#Run pip install flask-blueprint
from flask import Blueprint, render_template
from models import Booking, User, db
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, login_required, current_user, logout_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

driver = Blueprint('driver',__name__)

@driver.route('/driver_dashboard')
@login_required
def driver_dashboard():
    return render_template('driverarea.html', firstname=current_user.firstname, lastname=current_user.lastname)

@driver.route('/driver_profile')
@login_required
def driver_profile():
    users_profit = User.query.filter_by(id=current_user.id).first()
    update_agent_profile = [users_profit]
    return render_template('driver_profile.html', firstname=current_user.firstname, lastname=current_user.lastname,update_agent_profile=update_agent_profile)

@driver.route('/support')
@login_required
def driver_support():
    return render_template('driver_support.html', firstname=current_user.firstname, lastname=current_user.lastname)