from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100))
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    contact_address = db.Column(db.String(100))
    state = db.Column(db.String(100))
    lga = db.Column(db.String(100))
    next_of_kin_name = db.Column(db.String(100))
    next_of_kin_phone = db.Column(db.String(100))
    next_of_kin_contact = db.Column(db.String(100))
    bank_account = db.Column(db.String(100))
    bank_title = db.Column(db.String(100))
    bank_name = db.Column(db.String(100))
    user_status = db.Column(db.String(100))
    type_of_truck = db.Column(db.String(100))
    plate_number = db.Column(db.String(100))
    driving_license = db.Column(db.String(100))
    mean_of_id = db.Column(db.String(100))
    account_type = db.Column(db.String(100))
    register_date = db.Column(db.DateTime)
    booking_id =  db.relationship('Booking', backref='user', lazy="dynamic")

class Booking(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_of_goods = db.Column(db.String(100))
    destination = db.Column(db.String(100))
    location = db.Column(db.String(100))
    quantity = db.Column(db.String(100))
    date_time = db.Column(db.DateTime)
    approved_by =db.Column(db.String(100))
    order_status = db.Column(db.String(100))
    booking_code = db.Column(db.String(100))
    amount = db.Column(db.String(100))
    payment_date = db.Column(db.DateTime)
    state_origin = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
   
