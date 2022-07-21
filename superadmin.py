#Run pip install flask-blueprint
from flask import Blueprint
from flask import Flask,redirect,url_for,render_template,request, flash
import datetime
from models import User, Booking, db
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, login_required, current_user, logout_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
superadmin = Blueprint('superadmin',__name__)

@superadmin.route('/staff_register')
def staff_register():
    return render_template('registerstaff.html')

@superadmin.route('/create_account', methods=['POST'])
def create_account():
    fname = request.form.get('firstname')
    lname = request.form.get('lastname')
    email_id = request.form.get('email')
    password_id = request.form.get('password')
    account_type = request.form.get('account_type')
    users = User.query.filter_by(email=email_id).first()
    if users:
        return redirect(url_for('superadmin.staff_register'))
    register_date = datetime.datetime.utcnow()
    new_user =User(firstname=fname, lastname=lname, email=email_id, password=generate_password_hash(password_id,method='sha256'),account_type=account_type, register_date=register_date)
    db.session.add(new_user)
    db.session.commit()
    return "<h1>Staff account created!!<h1>"

@superadmin.route('/admin_panel')
@login_required
def adminpanel():
    getRequest = Booking.query.filter_by(order_status='pending').all()
    return render_template('staffdashboard.html', firstname=current_user.firstname, lastname=current_user.lastname, getRequest=getRequest)


@superadmin.route('/updatereq/<int:book_id>', methods=['GET'])
@login_required
def updatereq(book_id):
    updatebooking= Booking.query.get(int(book_id))
    getAgent=User.query.filter_by(account_type='Agent').all()
    something = [updatebooking]
    return render_template('staffupdaterequest.html',firstname=current_user.firstname, lastname=current_user.lastname,something=something, getAgent=getAgent)

@superadmin.route('/staffprofile')
@login_required
def staffprofile():
    users_profit = User.query.filter_by(id=current_user.id).first()
    update_agent_profile = [users_profit]
    return render_template('staffprofile.html', update_agent_profile=update_agent_profile)


@superadmin.route('/billing')
@login_required
def billing():
   
    return render_template('staffbilling.html', firstname=current_user.firstname, lastname=current_user.lastname)

@superadmin.route('/onboard_agent')
@login_required
def onboard_agent():
    return render_template('staffregisteragent.html', firstname=current_user.firstname, lastname=current_user.lastname)

@superadmin.route('/staffviewuser')
@login_required
def staffviewuser():
    return render_template('staffviewuser.html', firstname=current_user.firstname, lastname=current_user.lastname)

@superadmin.route('/staff_support')
@login_required
def staff_support():
    return render_template('staffsupport.html', firstname=current_user.firstname, lastname=current_user.lastname)

@superadmin.route('/requestupdate', methods=['POST'])
def requestupdate():
    book_id =request.form.get('id')
    booked=Booking.query.filter_by(id=book_id).first()
    booked.amount = request.form.get('amount')
    booked.order_status = request.form.get('order_status')
    db.session.commit()
    return redirect(url_for('superadmin.adminpanel', firstname=current_user.firstname, lastname=current_user.lastname) )

@superadmin.route('/staff_update_profile', methods=['POST'])
def staff_update_profile():
    staff_id = request.form.get('id')
    Update_staff =User.query.filter_by(id=staff_id).first()
    #Update_staff.firstname= request.form.get('firstname')
    #Update_staff.lastname = request.form.get('lastname')
    Update_staff.phone = request.form.get('phone')
    Update_staff.contact_address = request.form.get('contact_address')
    Update_staff.phone = request.form.get('lga')
    Update_staff.state= request.form.get('state')
    Update_staff.bank_account = request.form.get('bank_account')
    Update_staff.bank_title = request.form.get('bank_title')
    Update_staff.bank_name = request.form.get('bank_name')
    Update_staff.next_of_kin_name = request.form.get('next_of_kin_name')
    Update_staff.next_of_kin_phone= request.form.get('next_of_kin_phone')
    Update_staff.next_of_kin_contact = request.form.get('next_of_kin_contact')
    db.session.commit()
    return redirect(url_for('superadmin.adminpanel', firstname=current_user.firstname, lastname=current_user.lastname) )

    