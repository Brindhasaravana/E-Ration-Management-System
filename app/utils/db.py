from pymongo import MongoClient
from flask import current_app, g

def get_db():
    if 'db' not in g:
        client = MongoClient(current_app.config['MONGO_URI'])
        g.db = client[current_app.config['DB_NAME']]
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.client.close()

def init_db(app):
    with app.app_context():
        db = get_db()
        # Create indexes
        db.users.create_index('email', unique=True)
        db.shops.create_index('email', unique=True)
        
        # Create admin user if it doesn't exist
        if not db.users.find_one({'email': 'admin@example.com'}):
            admin_user = {
                'fullName': 'Admin User',
                'email': 'admin@example.com',
                'password': 'admin123',
                'userType': 'admin'
            }
            db.users.insert_one(admin_user) 