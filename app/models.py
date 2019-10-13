from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
    return Users.query.get(int(id))

# DB classess
class Users(UserMixin, db.Model):

    __tablename__ = 'users'
 
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(100))
    username = db.Column(db.String(30))
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(100))
    user_role = db.Column(db.String(30))
    date = db.Column(db.DateTime)
    
    def __init__(self, userid=None, username=None, email=None, password=None, user_role=None, date=None):
        self.userid = userid
        self.username = username
        self.email = email
        self.password = password
        self.user_role = user_role
        self.date = date

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Vehicles(db.Model):
    __tablename__ = 'vehicles'
 
    id = db.Column(db.Integer, primary_key=True)
    vehicle_number = db.Column(db.String(100),unique=True)
    vehicle_type = db.Column(db.String(30))
    vehicle_price = db.Column(db.Integer)
    vehicle_tankcapacity = db.Column(db.Integer)

    fuel_reg_rel = db.relationship('Fuel_reg', backref='fuel_reg_rel')
    oil_reg_rel = db.relationship('Oil_reg', backref='oil_reg_rel')
    general_expenses_reg_rel = db.relationship('General_expenses_reg', backref='general_expenses_reg_rel')
    tyre_reg_rel = db.relationship('Tyre_reg', backref='tyre_reg_rel')
    repair_local_reg_rel = db.relationship('Repair_local_reg', backref='repair_local_reg_rel')
    total_expense_rel = db.relationship('Total_expense', backref='total_expense_rel')

    
    def __init__(self, vehicle_number=None, vehicle_type=None, vehicle_price=None, vehicle_tankcapacity=None):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type
        self.vehicle_price = vehicle_price
        self.vehicle_tankcapacity = vehicle_tankcapacity

class Fuel_reg(db.Model):
    __tablename__ = 'fuel_reg'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    month = db.Column(db.String(30))
    year = db.Column(db.Integer)
    voucher_number = db.Column(db.String(100))
    liters = db.Column(db.Integer)
    driver_name = db.Column(db.String(100))
    cost = db.Column(db.Float(10, 2))
    purchased_from = db.Column(db.String(200))
    bill_filepath = db.Column(db.String(300))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))


    def __init__(self, date=None, month=None, year=None, voucher_number=None,
                liters=None,driver_name=None,cost=None, vehicle_id = None,
                purchased_from=None,bill_filepath=None ):
        self.date = date
        self.month = month
        self.year = year
        self.voucher_number = voucher_number
        self.liters = liters
        self.driver_name = driver_name
        self.cost = cost
        self.purchased_from = purchased_from
        self.bill_filepath = bill_filepath
        self.vehicle_id = vehicle_id

class Oil_reg(db.Model):
    __tablename__ = 'oil_reg'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    month = db.Column(db.String(30))
    year = db.Column(db.Integer)
    voucher_number = db.Column(db.String(100))
    engine_oil = db.Column(db.String(30))
    gear_oil = db.Column(db.String(30))
    grease_oil = db.Column(db.String(30))
    driver_name = db.Column(db.String(100))
    cost = db.Column(db.Float(10, 2))
    remark = db.Column(db.String(1000))
    bill_filepath = db.Column(db.String(300))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))

    def __init__(self, date=None, month=None, year=None, vehicle_id = None,
                voucher_number=None,engine_oil = None,
                gear_oil = None,grease_oil= None,
                driver_name = None,cost = None,remark = None,bill_filepath = None):
        self.date = date
        self.month = month
        self.year = year
        self.voucher_number = voucher_number
        self.engine_oil = engine_oil
        self.gear_oil = gear_oil
        self.grease_oil = grease_oil
        self.driver_name = driver_name
        self.cost = cost
        self.remark = remark
        self.bill_filepath = bill_filepath
        self.vehicle_id = vehicle_id

class General_expenses_reg(db.Model):
    __tablename__ = 'general_expenses_reg'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    month = db.Column(db.String(30))
    year = db.Column(db.Integer)
    voucher_number = db.Column(db.String(100))
    description_purchase = db.Column(db.String(300))
    driver_name = db.Column(db.String(100))
    cost = db.Column(db.Float(10, 2))
    remark = db.Column(db.String(1000))
    bill_filepath = db.Column(db.String(300))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))

    def __init__(self, date=None, month=None, year=None, voucher_number=None,
                description_purchase = None,driver_name = None,vehicle_id = None,
                cost= None,remark = None,bill_filepath = None):
        self.date = date
        self.month = month
        self.year = year
        self.voucher_number = voucher_number
        self.description_purchase = description_purchase
        self.driver_name = driver_name
        self.cost = cost
        self.remark = remark
        self.bill_filepath = bill_filepath
        self.vehicle_id = vehicle_id

class Tyre_reg(db.Model):
    __tablename__ = 'tyre_reg'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    month = db.Column(db.String(30))
    year = db.Column(db.Integer)
    voucher_number = db.Column(db.String(100))
    tyre_number = db.Column(db.String(100))
    date_of_issue = db.Column(db.DateTime)
    on_date = db.Column(db.DateTime)
    on_date_meter_reading = db.Column(db.Integer)
    off_date = db.Column(db.DateTime)
    off_date_meter_reading = db.Column(db.Integer)
    km_current_month = db.Column(db.Integer)
    front_rear = db.Column(db.String(30))
    removal_reason = db.Column(db.String(200))
    total_km = db.Column(db.Integer)
    cost = db.Column(db.Float(10, 2))
    bill_filepath = db.Column(db.String(300))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))

    def __init__(self, date=None, month=None, year=None, voucher_number=None,tyre_number = None,vehicle_id = None,
                date_of_issue = None,on_date= None,on_date_meter_reading = None, off_date=None, cost = None,
                off_date_meter_reading=None,km_current_month = None,front_rear = None,
                removal_reason= None,total_km = None, bill_filepath = None):
        self.date = date
        self.month = month
        self.year = year
        self.voucher_number = voucher_number
        self.tyre_number = tyre_number
        self.date_of_issue = date_of_issue
        self.on_date = on_date
        self.on_date_meter_reading = on_date_meter_reading
        self.off_date = off_date
        self.off_date_meter_reading = off_date_meter_reading
        self.km_current_month = km_current_month
        self.front_rear = front_rear
        self.removal_reason = removal_reason
        self.total_km = total_km
        self.cost = cost
        self.bill_filepath = bill_filepath
        self.vehicle_id = vehicle_id

class Repair_local_reg(db.Model):
    __tablename__ = 'repair_local_reg'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    month = db.Column(db.String(30))
    year = db.Column(db.Integer)
    serial_number = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    supplier = db.Column(db.String(100))
    cost = db.Column(db.Float(10, 2))
    sancation_number_date_bywhom = db.Column(db.String(200))
    date_of_supply = db.Column(db.DateTime)
    date_of_bill = db.Column(db.DateTime)
    fitted_place = db.Column(db.String(200))
    driver_name = db.Column(db.String(100))
    passed_amount = db.Column(db.Float(10, 2))
    c_bill_number = db.Column(db.String(200))
    remark = db.Column(db.String(1000))
    bill_filepath = db.Column(db.String(300))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))
    

    def __init__(self, date=None, month=None, year=None, serial_number=None,description = None,vehicle_id = None,
                supplier = None,cost= None,sancation_number_date_bywhom = None, date_of_supply=None, 
                fitted_place=None,driver_name = None,passed_amount = None,date_of_bill = None,
                c_bill_number= None,remark = None, bill_filepath = None):

        self.date = date
        self.month = month
        self.year = year
        self.serial_number = serial_number
        self.description = description
        self.supplier = supplier
        self.cost = cost
        self.sancation_number_date_bywhom = sancation_number_date_bywhom
        self.date_of_supply = date_of_supply
        self.date_of_bill = date_of_bill
        self.fitted_place = fitted_place
        self.driver_name = driver_name
        self.passed_amount = passed_amount
        self.c_bill_number = c_bill_number
        self.remark = remark
        self.bill_filepath = bill_filepath
        self.vehicle_id = vehicle_id


class Total_expense(db.Model):
    __tablename__ = 'total_expense'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    month = db.Column(db.String(30))
    year = db.Column(db.Integer)
    km_open = db.Column(db.Integer)
    km_close = db.Column(db.Integer)
    total_km_per_month = db.Column(db.Integer)
    km_government = db.Column(db.Integer)
    km_private = db.Column(db.Integer)
    fuel_consumption = db.Column(db.Integer)
    fuel_ceiling = db.Column(db.Integer)
    excess = db.Column(db.Integer)
    fuel_kmpl = db.Column(db.Integer)
    fuel_quantity = db.Column(db.Integer)
    lubricant_oil_kmpl = db.Column(db.Integer)
    lubricant_oil_quantity = db.Column(db.Integer)
    fuel_cost = db.Column(db.Float(10, 2))
    oil_cost = db.Column(db.Float(10, 2))
    general_expenses_cost = db.Column(db.Float(10, 2))
    tyre_cost = db.Column(db.Float(10, 2))
    repair_cost = db.Column(db.Float(10, 2))
    total_cost_this_month = db.Column(db.Float(10, 2))
    total_cost_till_month = db.Column(db.Float(10, 2))
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'))

    def __init__(self, date=None, month=None, year=None, km_open=None,km_close = None,vehicle_id = None,
                total_km_per_month = None,km_government= None,km_private = None, fuel_consumption=None, 
                fuel_ceiling=None,excess = None,fuel_kmpl = None,fuel_quantity=None,lubricant_oil_kmpl=None,
                lubricant_oil_quantity= None,fuel_cost = None, oil_cost = None,general_expenses_cost=None,tyre_cost=None,
                repair_cost=None,total_cost_this_month=None,total_cost_till_month=None):

        self.date = date
        self.month = month
        self.year = year
        self.km_open = km_open
        self.km_close = km_close
        self.total_km_per_month = total_km_per_month
        self.km_government = km_government
        self.km_private = km_private
        self.fuel_consumption = fuel_consumption
        self.fuel_ceiling = fuel_ceiling
        self.excess = excess
        self.fuel_kmpl = fuel_kmpl
        self.fuel_quantity = fuel_quantity
        self.lubricant_oil_kmpl = lubricant_oil_kmpl
        self.lubricant_oil_quantity = lubricant_oil_quantity
        self.fuel_cost = fuel_cost
        self.oil_cost = oil_cost
        self.general_expenses_cost = general_expenses_cost
        self.tyre_cost = tyre_cost
        self.repair_cost = repair_cost
        self.total_cost_this_month = total_cost_this_month
        self.total_cost_till_month = total_cost_till_month
        self.vehicle_id = vehicle_id



# db.create_all()