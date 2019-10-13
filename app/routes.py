from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, RegistrationForm, VehicleAddForm, FuelRegAddForm, OilRegAddForm, GenExpRegAddForm, TyreRegAddForm, RepairRegAddForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Users, Vehicles, Fuel_reg, Oil_reg, General_expenses_reg, Tyre_reg, Repair_local_reg
from werkzeug.urls import url_parse
from app import db
import datetime



@app.route('/')
@app.route('/index')
@login_required
def index():
    # user = {'username': 'Vishno Prasad'}
    return render_template("index.html", title='Home Page')

@app.route('/admin')
@login_required
def admin():
    # user = {'username': 'Vishno Prasad'}
    return render_template("admin.html", title='Home Page')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    # if current_user.is_authenticated and current_user.user_role == 'admin':
    #     return redirect(url_for('admin'))
    # if current_user.is_authenticated and current_user.user_role == 'user':
    #     return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        # next_page = request.args.get('next')
        # if not next_page or url_parse(next_page).netloc != '' :
        #     if user.user_role == 'admin':
        #         print('user role: ',user.user_role)
        #         next_page = url_for('admin')
        #     elif user.user_role == 'user':
        #         print('user role: ',user.user_role)
        #         next_page = url_for('index')
        if user.user_role == 'admin':
            print('user role: ',user.user_role)
            next_page = url_for('admin')
        elif user.user_role == 'user':
            print('user role: ',user.user_role)
            next_page = url_for('index')   
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('register'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Users(userid = form.userid.data, username=form.username.data, email=form.email.data, user_role = form.user_role.data, date = form.date.data,)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/VehicleAdd', methods=['GET', 'POST'])
def VehicleAdd():
    if current_user.is_authenticated:
        return redirect(url_for('VehicleAdd'))
    form = VehicleAddForm()
    if form.validate_on_submit():
        vehicle = Vehicles(vehicle_number = (form.vehicle_number.data).upper().strip(), vehicle_type=form.vehicle_type.data, vehicle_price=form.vehicle_price.data, vehicle_tankcapacity = form.vehicle_tankcapacity.data)
        db.session.add(vehicle)
        db.session.commit()
        flash('Vehicle information has been added')
        return redirect(url_for('login'))
    return render_template('vehicle_add.html', title='Vehicle Add', form=form)

@app.route('/FuelRegAdd', methods=['GET', 'POST'])
def FuelRegAdd():
    if current_user.is_authenticated:
        return redirect(url_for('FuelRegAdd'))
    form = FuelRegAddForm()
    if form.validate_on_submit():
        date_data = str((form.date.data)).split('-')
        year = int(date_data[0])
        month = int(date_data[1])
        month_name = datetime.date(year, month, 1).strftime('%B')
        vehicleData = Vehicles.query.filter_by(vehicle_number=(form.vehicle_number.data).upper().strip()).first()

        fuel_reg = Fuel_reg(date = form.date.data, month=month_name, year=year, voucher_number = form.voucher_number.data, liters = form.liters.data, 
                            driver_name = form.driver_name.data, cost = form.cost.data, purchased_from = form.purchased_from.data, bill_filepath = form.bill_filepath.data, vehicle_id = vehicleData.id )
        db.session.add(fuel_reg)
        db.session.commit()
        flash('Fuel information has been added')
        return redirect(url_for('login'))
    return render_template('fuel_reg.html', title='Fuel Registration', form=form)

@app.route('/OilRegAdd', methods=['GET', 'POST'])
def OilRegAdd():
    if current_user.is_authenticated:
        return redirect(url_for('OilRegAdd'))
    form = OilRegAddForm()
    if form.validate_on_submit():
        date_data = str((form.date.data)).split('-')
        year = int(date_data[0])
        month = int(date_data[1])
        month_name = datetime.date(year, month, 1).strftime('%B')
        vehicleData = Vehicles.query.filter_by(vehicle_number=(form.vehicle_number.data).upper().strip()).first()

        oil_reg = Oil_reg(date = form.date.data, month=month_name, year=year, voucher_number = form.voucher_number.data, engine_oil = form.engine_oil.data, remark= form.remark.data, bill_filepath = form.bill_filepath.data,
                            gear_oil = form.gear_oil.data, grease_oil = form.grease_oil.data, driver_name = form.driver_name.data, cost = form.cost.data, vehicle_id = vehicleData.id )
        db.session.add(oil_reg)
        db.session.commit()
        flash('Oil information has been added')
        return redirect(url_for('login'))
    return render_template('oil_reg.html', title='Oil Registration', form=form)

@app.route('/GeneralExpenseRegAdd', methods=['GET', 'POST'])
def GeneralExpenseRegAdd():
    if current_user.is_authenticated:
        return redirect(url_for('GeneralExpenseRegAdd'))
    form = GenExpRegAddForm()
    if form.validate_on_submit():
        date_data = str((form.date.data)).split('-')
        year = int(date_data[0])
        month = int(date_data[1])
        month_name = datetime.date(year, month, 1).strftime('%B')
        vehicleData = Vehicles.query.filter_by(vehicle_number=(form.vehicle_number.data).upper().strip()).first()

        gen_exp_reg = General_expenses_reg(date = form.date.data, month=month_name, year=year, voucher_number = form.voucher_number.data, description_purchase = form.description_purchase.data,
                            driver_name = form.driver_name.data, cost = form.cost.data, remark = form.remark.data, vehicle_id = vehicleData.id, bill_filepath = form.bill_filepath.data )
        db.session.add(gen_exp_reg)
        db.session.commit()
        flash('General Expense information has been added')
        return redirect(url_for('login'))
    return render_template('gen_exp_reg.html', title='General Expense Registration', form=form)

@app.route('/TyreRegAdd', methods=['GET', 'POST'])
def TyreRegAdd():
    if current_user.is_authenticated:
        return redirect(url_for('TyreRegAdd'))
    form = TyreRegAddForm()
    if form.validate_on_submit():
        date_data = str((form.date.data)).split('-')
        year = int(date_data[0])
        month = int(date_data[1])
        month_name = datetime.date(year, month, 1).strftime('%B')
        vehicleData = Vehicles.query.filter_by(vehicle_number=(form.vehicle_number.data).upper().strip()).first()

        tyre_reg = Tyre_reg(date = form.date.data, month=month_name, year=year, voucher_number = form.voucher_number.data, tyre_number = form.tyre_number.data,
                            date_of_issue = form.date_of_issue.data, on_date = form.on_date.data, on_date_meter_reading = form.on_date_meter_reading.data, vehicle_id = vehicleData.id, off_date = form.off_date.data,
                            off_date_meter_reading = form.off_date_meter_reading.data, km_current_month = form.km_current_month.data, front_rear = form.front_rear.data,
                            removal_reason= form.removal_reason.data, total_km = form.total_km.data , cost = form.cost.data, bill_filepath = form.bill_filepath.data )
        db.session.add(tyre_reg)
        db.session.commit()
        flash('Tyre information has been added')
        return redirect(url_for('login'))
    return render_template('tyre_reg.html', title='Tyre Registration', form=form)

@app.route('/RepairRegAdd', methods=['GET', 'POST'])
def RepairRegAdd():
    if current_user.is_authenticated:
        return redirect(url_for('RepairRegAdd'))
    form = RepairRegAddForm()
    if form.validate_on_submit():
        date_data = str((form.date.data)).split('-')
        year = int(date_data[0])
        month = int(date_data[1])
        month_name = datetime.date(year, month, 1).strftime('%B')
        vehicleData = Vehicles.query.filter_by(vehicle_number=(form.vehicle_number.data).upper().strip()).first()

        repair_reg = Repair_local_reg(date = form.date.data, month=month_name, year=year, serial_number = form.serial_number.data, description = form.description.data,
                            supplier = form.supplier.data, cost = form.cost.data, sancation_number_date_bywhom = form.sancation_number_date_bywhom.data, vehicle_id = vehicleData.id, date_of_supply = form.date_of_supply.data,
                            date_of_bill = form.date_of_bill.data, fitted_place = form.fitted_place.data, driver_name = form.driver_name.data,
                            passed_amount= form.passed_amount.data, c_bill_number = form.c_bill_number.data , remark = form.remark.data, bill_filepath = form.bill_filepath.data )
        db.session.add(repair_reg)
        db.session.commit()
        flash('repair information has been added')
        return redirect(url_for('login'))
    return render_template('repair_reg.html', title='Repair Registration', form=form)