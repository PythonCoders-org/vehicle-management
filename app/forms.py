from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, SelectField, IntegerField, FloatField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
import datetime
from app.models import Users, Vehicles

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class RegistrationForm(FlaskForm):
    userid = StringField('User ID', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    user_role = StringField('User Role', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    date = DateTimeField('Date & Time', default=datetime.datetime.now())
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class VehicleAddForm(FlaskForm):
    vehicle_number = StringField('Vehicle Number', validators=[DataRequired()])
    vehicle_type = SelectField('Vehicle Type', choices = [('Petrol', 'Petrol'), 
      ('Diesel', 'Diesel')])
    vehicle_price = IntegerField('Vehicle Price', validators=[DataRequired()])
    vehicle_tankcapacity = IntegerField('Tank Capacity', validators=[DataRequired()])
    submit = SubmitField('submit')


    def validate_vehicleNumber(self, vehicle_number):
        vehicleNumber = Vehicles.query.filter_by(vehicle_number=(vehicle_number.data).upper().strip()).first()
        if vehicleNumber is not None:
            raise ValidationError('Vehicle Number is Already Exist')

class FuelRegAddForm(FlaskForm):
    vehicle_number = StringField('Vehicle Number', validators=[DataRequired()])
    date = DateTimeField('Date & Time', default=datetime.datetime.now())
    voucher_number = StringField('Voucher Number')
    liters = IntegerField('Liters', validators=[DataRequired()])
    driver_name = StringField('Driver Name', validators=[DataRequired()])
    cost = FloatField('Cost', validators=[DataRequired()])
    purchased_from = StringField('purchased_from', validators=[DataRequired()])
    bill_filepath = StringField('bill_filepath')
    submit = SubmitField('submit')

    def validate_vehicleNumber(self, vehicle_number):
        vehicleNumber = Vehicles.query.filter_by(vehicle_number=(vehicle_number.data).upper().strip()).first()
        if vehicleNumber is None:
            raise ValidationError('Vehicle Number Not Found in database')

class OilRegAddForm(FlaskForm):
    vehicle_number = StringField('Vehicle Number', validators=[DataRequired()])
    date = DateTimeField('Date & Time', default=datetime.datetime.now())
    voucher_number = StringField('Voucher Number')
    engine_oil = StringField('Engine Oil')
    gear_oil = StringField('Gear Oil')
    grease_oil = StringField('Grease Oil')
    driver_name = StringField('Driver Name', validators=[DataRequired()])
    cost = FloatField('Cost', validators=[DataRequired()])
    remark = StringField('Remark')
    bill_filepath = StringField('Bill photo')
    submit = SubmitField('submit')

    def validate_vehicleNumber(self, vehicle_number):
        vehicleNumber = Vehicles.query.filter_by(vehicle_number=(vehicle_number.data).upper().strip()).first()
        if vehicleNumber is not None:
            raise ValidationError('Vehicle Number Not Found in database')

class GenExpRegAddForm(FlaskForm):
    vehicle_number = StringField('Vehicle Number', validators=[DataRequired()])
    date = DateTimeField('Date & Time', default=datetime.datetime.now())
    voucher_number = StringField('Voucher Number')
    description_purchase = StringField('Description Purchase')
    driver_name = StringField('Driver Name', validators=[DataRequired()])
    cost = FloatField('Cost', validators=[DataRequired()])
    remark = StringField('Remark')
    bill_filepath = StringField('Bill photo')
    submit = SubmitField('submit')

    def validate_vehicleNumber(self, vehicle_number):
        vehicleNumber = Vehicles.query.filter_by(vehicle_number=(vehicle_number.data).upper().strip()).first()
        if vehicleNumber is not None:
            raise ValidationError('Vehicle Number Not Found in database')

class TyreRegAddForm(FlaskForm):
    vehicle_number = StringField('Vehicle Number', validators=[DataRequired()])
    date = DateTimeField('Date & Time', default=datetime.datetime.now())
    voucher_number = StringField('Voucher Number')
    tyre_number = StringField('Tyre Number')
    date_of_issue = DateTimeField('Date of Issue', default=datetime.datetime.now())
    on_date = DateTimeField('On Date', default=datetime.datetime.now())
    on_date_meter_reading = IntegerField('On Date Meter Reading')
    off_date = DateTimeField('Off Date', default=datetime.datetime.now())
    off_date_meter_reading = IntegerField('Off Date Meter Reading')
    km_current_month = IntegerField('Km Current Month')
    front_rear = SelectField('Front/Rear', choices = [('Front Right', 'Front Right'), ('Front Left', 'Front Left'), 
      ('Rear Right', 'Rear Right'), ('Rear Left', 'Rear Left') ])
    removal_reason = StringField('Reason For Removal')
    cost = FloatField('Cost', validators=[DataRequired()])
    total_km = IntegerField('Total Km')
    bill_filepath = StringField('Bill photo')
    submit = SubmitField('submit')

    def validate_vehicleNumber(self, vehicle_number):
        vehicleNumber = Vehicles.query.filter_by(vehicle_number=(vehicle_number.data).upper().strip()).first()
        if vehicleNumber is not None:
            raise ValidationError('Vehicle Number Not Found in database')

class RepairRegAddForm(FlaskForm):
    vehicle_number = StringField('Vehicle Number', validators=[DataRequired()])
    date = DateTimeField('Date & Time', default=datetime.datetime.now())
    serial_number = StringField('Serial Number')
    description = StringField('Description')
    supplier = StringField('Supplier')
    sancation_number_date_bywhom = StringField('Sancation Number Date By Whom')
    date_of_supply = DateTimeField('Date of Supply', default=datetime.datetime.now())
    date_of_bill = DateTimeField('Date of Bill', default=datetime.datetime.now())
    fitted_place = StringField('Fitted Place')
    driver_name = StringField('Driver Name')
    passed_amount = FloatField('Passed Amount')
    c_bill_number = StringField('C Bill Number')
    cost = FloatField('Cost')
    remark = StringField('Remark')
    bill_filepath = StringField('Bill photo')
    submit = SubmitField('submit')

    def validate_vehicleNumber(self, vehicle_number):
        vehicleNumber = Vehicles.query.filter_by(vehicle_number=(vehicle_number.data).upper().strip()).first()
        if vehicleNumber is not None:
            raise ValidationError('Vehicle Number Not Found in database')