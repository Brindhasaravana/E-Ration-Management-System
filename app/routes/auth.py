from flask import Blueprint, request, jsonify, session
from app.utils.db import get_db

auth_bp = Blueprint('auth', __name__, url_prefix='/api')

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    db = get_db()
    
    if db.users.find_one({'email': data['email']}):
        return jsonify({'message': 'Email already registered'}), 400
    
    user = {
        'fullName': data['fullName'],
        'email': data['email'],
        'aadhar': data['aadhar'],
        'password': data['password'],
        'userType': 'user'
    }
    
    try:
        db.users.insert_one(user)
        return jsonify({'message': 'Registration successful'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    db = get_db()
    
    user = db.users.find_one({
        'email': data['email'],
        'password': data['password']
    })
    
    if user:
        session['user_id'] = str(user['_id'])
        session['userType'] = user.get('userType', 'user')
        
        return jsonify({
            'message': 'Login successful',
            'userType': user.get('userType', 'user')
        }), 200
    else:
        return jsonify({'message': 'Invalid email or password'}), 401 