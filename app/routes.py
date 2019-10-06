from flask import render_template, flash, redirect, url_for, request
from app import app
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import Users
from werkzeug.urls import url_parse
from app import db


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