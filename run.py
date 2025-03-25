from app import create_app
from datetime import datetime, timedelta
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_session import Session
import os

app = create_app()

# Configure Flask-Session
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-here')
app.config['SESSION_PERMANENT'] = False
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)

# Initialize Flask-Session
Session(app)

class ProductRequest:
    def __init__(self, product, quantity, date=None, status="Pending"):
        self.product = product
        self.quantity = quantity
        self.date = date or datetime.now()
        self.status = status

@app.route('/request-product', methods=['POST'])
def request_product():
    if request.method == 'POST':
        product = request.form.get('product')
        quantity = request.form.get('quantity')
        
        if not product or not quantity:
            flash('Please fill in all fields', 'error')
            return redirect(url_for('dashboard'))
        
        try:
            # Initialize the requests list if it doesn't exist
            if 'product_requests' not in session:
                session['product_requests'] = []
            
            new_request = {
                'product': product,
                'quantity': float(quantity),
                'date': datetime.now(),
                'status': 'Pending'
            }
            
            current_requests = session.get('product_requests', [])
            current_requests.append(new_request)
            session['product_requests'] = current_requests
            session.modified = True
            
            flash('Product request submitted successfully!', 'success')
        except Exception as e:
            flash(f'Error submitting request: {str(e)}', 'error')
            
        return redirect(url_for('dashboard'))

@app.route('/dashboard')
def dashboard():
    requests = session.get('product_requests', [])
    return render_template('dashboard.html', requests=requests)

if __name__ == '__main__':
    app.run(debug=True) 