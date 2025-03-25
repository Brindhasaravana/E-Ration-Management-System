from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from . import db
from .models import User, ProductRequest

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@main.route('/request-product', methods=['POST'])
@login_required
def request_product():
    product = request.form.get('product')
    quantity = request.form.get('quantity')
    
    if not product or not quantity:
        flash('Please fill in all fields', 'error')
        return redirect(url_for('main.dashboard'))
    
    try:
        quantity = int(quantity)
        if quantity <= 0 or quantity > 25:
            flash('Invalid quantity. Please enter a value between 1 and 25', 'error')
            return redirect(url_for('main.dashboard'))
            
        new_request = ProductRequest(
            user_id=current_user.id,
            product_name=product,
            quantity=quantity,
            status='pending'
        )
        
        db.session.add(new_request)
        db.session.commit()
        
        flash(f'Successfully requested {quantity}kg of {product}', 'success')
        
    except ValueError:
        flash('Invalid quantity value', 'error')
    
    return redirect(url_for('main.dashboard')) 