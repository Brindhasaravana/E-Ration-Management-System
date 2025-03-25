from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        if not email or not password:
            flash('Please enter both email and password', 'error')
            return redirect(url_for('auth.login'))

        user = User.query.filter_by(email=email).first()

        if not user:
            flash('No account found with that email address', 'error')
            return redirect(url_for('auth.login'))

        if check_password_hash(user.password, password):
            login_user(user, remember=remember)
            flash(f'Welcome back, {user.name}!', 'success')
            return redirect(url_for('main.dashboard'))
        else:
            flash('Incorrect password', 'error')
            return redirect(url_for('auth.login'))

    return render_template('login.html')

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        smart_card = request.form.get('smart_card')
        phone = request.form.get('phone')

        # Validation checks
        if not all([email, name, password, confirm_password, smart_card, phone]):
            flash('Please fill in all fields', 'error')
            return redirect(url_for('auth.register'))

        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('auth.register'))

        # Check if email already exists
        if User.query.filter_by(email=email).first():
            flash('Email address already exists', 'error')
            return redirect(url_for('auth.register'))

        # Check if smart card number already exists
        if User.query.filter_by(smart_card=smart_card).first():
            flash('Smart card number already registered', 'error')
            return redirect(url_for('auth.register'))

        # Create new user
        new_user = User(
            email=email,
            name=name,
            smart_card=smart_card,
            phone=phone,
            password=generate_password_hash(password, method='scrypt')
        )

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please login with your email and password.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash('An error occurred. Please try again.', 'error')
            return redirect(url_for('auth.register'))

    return render_template('register.html')

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out successfully.', 'success')
    return redirect(url_for('main.index')) 