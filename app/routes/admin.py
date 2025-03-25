from flask import Blueprint, request, jsonify, session
from app.utils.db import get_db
from bson import ObjectId

admin_bp = Blueprint('admin', __name__, url_prefix='/api')

def admin_required(f):
    def wrapper(*args, **kwargs):
        if 'user_id' not in session or session.get('userType') != 'admin':
            return jsonify({'message': 'Unauthorized'}), 401
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper

@admin_bp.route('/create_shop', methods=['POST'])
@admin_required
def create_shop():
    data = request.json
    db = get_db()
    
    shop = {
        'name': data['name'],
        'email': data['email'],
        'city': data['city'],
        'contact': data['contact'],
        'aadhar': data['aadhar'],
        'userType': 'shopkeeper'
    }
    
    try:
        db.users.insert_one({
            'fullName': data['name'],
            'email': data['email'],
            'password': data['password'],
            'userType': 'shopkeeper'
        })
        
        db.shops.insert_one(shop)
        return jsonify({'message': 'Shop created successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@admin_bp.route('/assign_product', methods=['POST'])
@admin_required
def assign_product():
    data = request.json
    db = get_db()
    
    try:
        db.assignments.insert_one({
            'userId': data['userId'],
            'productId': data['productId'],
            'quantity': data['quantity']
        })
        return jsonify({'message': 'Product assigned successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@admin_bp.route('/users', methods=['GET'])
@admin_required
def get_users():
    db = get_db()
    
    try:
        users = list(db.users.find({'userType': 'user'}))
        for user in users:
            user['_id'] = str(user['_id'])
        return jsonify(users), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500 