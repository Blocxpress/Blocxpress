from flask import Blueprint
from flask import Flask,redirect,url_for,render_template,request, flash
import datetime
from models import User, Booking, db
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, login_required, current_user, logout_user, LoginManager
from werkzeug.security import generate_password_hash, check_password_hash
client = Blueprint('client',__name__)


#load client dashboard
@client.route('/clientarea')
@login_required
def clientarea():
    getRequest = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template('clientarea.html', firstname=current_user.firstname, lastname=current_user.lastname, getRequest=getRequest)

#load client registration form
@client.route('/registerclient')
def regclient():
    return render_template('registerclient.html')

#Booking 
@client.route('/booking', methods=['POST'])
def booking():
    goods_type = request.form.get('type_of_goods')
    quantity = request.form.get('quantity')
    goods_loc = request.form.get('goods_loc')
    destination = request.form.get('destination')
    book_date = request.form.get('book_date')
    state_of_origin = request.form.get('states_of_nigeria')
    new_book =Booking(type_of_goods=goods_type, quantity=quantity, destination=destination, location=goods_loc, date_time=book_date, order_status="Pending", state_origin=state_of_origin, user_id=current_user.id)
    db.session.add(new_book)
    db.session.commit()
    return redirect(url_for('client.clientarea'))

#Process use registration   
@client.route('/processclient', methods=['POST'])
def processclient():
    fname = request.form.get('firstname')
    lname = request.form.get('lastname')
    email_id = request.form.get('email')
    password_id = request.form.get('password')
    account_type = request.form.get('account_type')
    users = User.query.filter_by(email=email_id).first()
    if users:
        flash("Email address exist, try again using a different email address")
        return redirect(url_for('client.regclient'))
    register_date = datetime.datetime.utcnow()
    new_user =User(firstname=fname, lastname=lname, email=email_id, password=generate_password_hash(password_id,method='sha256'),account_type=account_type, register_date=register_date)
    db.session.add(new_user)
    db.session.commit()
    return render_template('confirmation.html', fname=fname)

    #userList = users.query.join(friendships, users.id==friendships.user_id)
    # .add_columns(users.userId, users.name, users.email, friends.userId, friendId)
    # .filter(users.id == friendships.friend_id)
    # .filter(friendships.user_id == userID).paginate(page, 1, False)