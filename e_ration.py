from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import pymysql

app = Flask(__name__)
api = Api(app)

# Database Configuration
db_config = {
    "host": "localhost",
    "user": "root",  # Change if needed
    "password": "",  # Change if needed
    "database": "e_ration",
}

def connect_db():
    try:
        conn = pymysql.connect(**db_config)
        return conn
    except Exception as e:
        return None

# Function to check database connection
@app.route('/check-db', methods=['GET'])
def check_db_connection():
    conn = connect_db()
    if conn:
        conn.close()
        return jsonify({"message": "Database is connected successfully"}), 200
    else:
        return jsonify({"message": "Failed to connect to database"}), 500
    
def getByVillageId(vId):
    if not vId or (isinstance(vId, str) and not vId.strip()):
        print("String is empty or invalid")
        return False  # Corrected False

    conn = connect_db()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        cursor.execute("SELECT * FROM store WHERE village_id = %s", (vId,))  # Fixed tuple issue
        store = cursor.fetchone()
        conn.close()
        return bool(store)  # Returns True if user exists, otherwise False

    except Exception as e:
        print("Database error:", str(e))
        return False  # Handle errors safely

    
@app.route('/store/add', methods=['POST'])
def addStore():
    conn = connect_db()
    if conn:
            data = request.get_json()
            vid = data.get("village_id")
            store = data.get("store_name")
            if getByVillageId(vid)==False:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO store (store_name, village_id) VALUES (%s, %s)", (store, vid))
                conn.commit()
                conn.close()
                return jsonify({"message": "Store is successfully inserted"}), 200
            else:
                return jsonify({"message": "village id already exists"}), 500
    else:
            return jsonify({"message": "Failed to connect to database"}), 500
    

@app.route('/store/getById', methods=['POST'])
def getStore():
    conn = connect_db()
    if conn:
            data = request.get_json()
            vid = data.get("village_id")
            if getByVillageId(vid):
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM store WHERE village_id = %s", (vid))
                store = cursor.fetchone()
                conn.close()
                return jsonify(store)
            else:
                return jsonify({"message": "village id not exists"}), 500
    else:
            return jsonify({"message": "Failed to connect to database"}), 500
        

@app.route('/store/getAll', methods=['GET'])
def getAllStore():
    conn = connect_db()
    if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM store")
                stores = cursor.fetchall()
                conn.close()
                if not stores:
                    return jsonify({"message": "village not exists"}), 500
                else:
                    return jsonify(stores)
    else:
            return jsonify({"message": "Failed to connect to database"}), 500     
        
    
@app.route('/store/update', methods=['POST'])
def updateStore():
    conn = connect_db()
    if conn:
            data = request.get_json()
            vid = data.get("village_id")
            store = data.get("store_name")
            if getByVillageId(vid):
                cursor = conn.cursor()
                cursor.execute("UPDATE store SET store_name=%s WHERE village_id=%s", (store, vid))
                conn.commit()
                conn.close()
                return jsonify({"message": "Store is successfully updated"}), 200
            else:
                return jsonify({"message": "village id not exists"}), 500
    else:
            return jsonify({"message": "Failed to connect to database"}), 500
        
@app.route('/store/delete', methods=['POST'])
def deleteStore():
    conn = connect_db()
    if conn:
            data = request.get_json()
            vid = data.get("village_id")
            if getByVillageId(vid):
                cursor = conn.cursor()
                cursor.execute("DELETE FROM store WHERE village_id = %s", (vid))
                conn.commit()
                conn.close()
                return jsonify({"message": "Store is successfully deleted"}), 200
            else:
                return jsonify({"message": "village id not exists"}), 500
    else:
            return jsonify({"message": "Failed to connect to database"}), 500   
        

def checkAdmindetails(phone, email):
    if not email or (isinstance(email, str) and not email.strip()):
        print("email is empty or invalid")
        return False  # Corrected False
    if not phone or (isinstance(phone, str) and not phone.strip()):
        print("phone is empty or invalid")
        return False  # Corrected False
    
    conn = connect_db()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        cursor.execute("SELECT * FROM admin WHERE phone_no = %s or email_id = %s", (phone,email))  # Fixed tuple issue
        store = cursor.fetchone()
        conn.close()
        return bool(store)  # Returns True if user exists, otherwise False

    except Exception as e:
        print("Database error:", str(e))
        return False  # Handle errors safely        



def checkStoreAssigned(store):
    if not store or (isinstance(store, str) and not store.strip()):
        print("store id is empty or invalid")
        return False  # Corrected False
    
    conn = connect_db()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        cursor.execute("SELECT * FROM admin WHERE store_id = %s", (store))  # Fixed tuple issue
        store = cursor.fetchone()
        conn.close()
        return bool(store)  # Returns True if user exists, otherwise False

    except Exception as e:
        print("Database error:", str(e))
        return False  # Handle errors safely            
        
@app.route('/admin/add', methods=['POST'])
def addAdmin():
    conn = connect_db()
    if conn:
            data = request.get_json()
            name = data.get("name")
            phone = data.get("phone_no")
            email = data.get("email_id")
            store = data.get("store_id")
            password = data.get("password")
            if checkAdmindetails(phone, email)==False:
                if checkStoreAssigned(store)==False:
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO admin (name, phone_no, email_id, store_id, password) VALUES (%s, %s,%s,%s,%s)",(name, phone, email, store, password))
                    conn.commit()
                    conn.close()
                    return jsonify({"message": "admin is successfully inserted"}), 200
                else:
                     return jsonify({"message": "store id already exists"}), 500
            else:
                return jsonify({"message": "admin details already exists"}), 500
    else:
            return jsonify({"message": "Failed to connect to database"}), 500                
     
     
def checkAdminExsits(empId):
    conn = connect_db()
    value = 'valid'
    if conn:
        if not empId or (isinstance(empId, str) and not empId.strip()):
            value = 'invalid'
        if value =='valid':
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM admin WHERE emp_id = %s", (empId))
            store = cursor.fetchone()
            conn.close()
            return jsonify(store)
    else:
        None
 

@app.route('/admin/getAll', methods=['GET'])
def getAllAdmin():
    conn = connect_db()
    if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM admin")
                admin = cursor.fetchall()
                conn.close()
                if not admin:
                    return jsonify({"message": "admin not exists"}), 500
                else:
                    return jsonify(admin)
    else:
            return jsonify({"message": "Failed to connect to database"}), 500 
        
        
@app.route('/admin/update', methods=['POST'])
def updateAdmin():
    conn = connect_db()
    if conn:
            data = request.get_json()
            empId = data.get("emp_id")
            name = data.get("name")
            phone = data.get("phone_no")
            email = data.get("email_id")
            store = data.get("store_id")
            password = data.get("password")
            if checkAdminExsits(empId) is not None:
                cursor = conn.cursor()
                cursor.execute("UPDATE admin SET name=%s,phone_no=%s, email_id=%s, password =%s, store_id=%s  WHERE emp_id=%s", (name, phone,email,password,store,empId))
                conn.commit()
                conn.close()
                return jsonify({"message": "Store is successfully updated"}), 200
            else:
                return jsonify({"message": "admin not exists"}), 500
    else:
            return jsonify({"message": "Failed to connect to database"}), 500
                
        
@app.route('/admin/getById', methods=['POST'])
def getAdmin():
    conn = connect_db()
    if conn:
            data = request.get_json()
            empId = data.get("emp_id")
            value = 'valid'
            if not empId or (isinstance(empId, str) and not empId.strip()):
                value = 'invalid'
            if value =='valid':
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM admin WHERE emp_id = %s", (empId))
                store = cursor.fetchone()
                conn.close()
                if store is None:
                    return  jsonify({"message": "admin not exists or invalid id"}), 500
                else:
                    return jsonify(store)
            else:
                return jsonify({"message": "admin not exists or invalid id"}), 500
    else:
            return jsonify({"message": "Failed to connect to database"}), 500


       
@app.route('/admin/delete', methods=['POST'])
def deleteAdmin():
    conn = connect_db()
    if conn:
            data = request.get_json()
            empId = data.get("emp_id")
            if checkAdminExsits(empId) is not None:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM admin WHERE emp_id = %s", (empId))
                conn.commit()
                conn.close()
                return jsonify({"message": "Admin is successfully deleted"}), 200
            else:
                return jsonify({"message": "Admin not exists"}), 500
    else:
            return jsonify({"message": "Failed to connect to database"}), 500   
        
#-----------------------------------
def checkCustExsits(custId, storeId):
    conn = connect_db()
    value =False
    if conn:
        if not custId or (isinstance(custId, str) and not custId.strip()):
            return False
        else:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customer WHERE ration_id = %s and store_id= %s", (custId,storeId))
            cust = cursor.fetchone()
            conn.close()
            if cust is None:
                return False
            else:
                return True


        
@app.route('/cust/add', methods=['POST'])
def addCust():
    conn = connect_db()
    if conn:
            data = request.get_json()
            ratId = data.get("ration_id")
            name = data.get("name")
            phone = data.get("phone_no")
            store = data.get("store_id")
            ratType = data.get("ration_type")
            address = data.get("address")
            members = data.get("members")
            lname = data.get("last_name")
            dob =data.get("dob")
            totalMem = data.get("total_mem")
            password = data.get("password")
            if checkCustExsits(ratId,store)==False:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO customer (ration_id,name, phone_no, store_id,ration_type,address,members,last_name,dob,total_mem, password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (ratId,name, phone, store,ratType,address,members,lname,dob,totalMem,password))
                conn.commit()
                conn.close()
                return jsonify({"message": "customer is successfully inserted"}), 200
            else:
                return jsonify({"message": "customer already exists"}), 500
    else:
            return jsonify({"message": "Failed to connect to database"}), 500 
        
@app.route('/cust/update', methods=['POST'])
def updateCust():
    conn = connect_db()
    if conn:
            data = request.get_json()
            ratId = data.get("ration_id")
            name = data.get("name")
            phone = data.get("phone_no")
            store = data.get("store_id")
            ratType = data.get("ration_type")
            address = data.get("address")
            members = data.get("members")
            lname = data.get("last_name")
            dob =data.get("dob")
            totalMem = data.get("total_mem")
            password = data.get("password")
            if checkCustExsits(ratId,store)==True:
                cursor = conn.cursor()
                cursor.execute("UPDATE customer SET name=%s,phone_no=%s, store_id =%s,ration_type =%s, address=%s,members =%s, last_name=%s,dob=%s,total_mem=%s,password=%s WHERE ration_id=%s", 
                               (name, phone, store,ratType,address,members,lname,dob,totalMem,password,ratId))
                conn.commit()
                conn.close()
                return jsonify({"message": "customer is successfully updated"}), 200
            else:
                return jsonify({"message": "customer not exists"}), 500
    else:
            return jsonify({"message": "Failed to connect to database"}), 500


@app.route('/cust/delete', methods=['POST'])
def deleteCust():
    conn = connect_db()
    if conn:
            data = request.get_json()
            rationid = data.get("ration_id")
            store = data.get("store_id")
            if checkCustExsits(rationid,store)==True:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM customer WHERE ration_id = %s and store_id=%s ", (rationid, store))
                conn.commit()
                conn.close()
                return jsonify({"message": "customer is successfully deleted"}), 200
            else:
                return jsonify({"message": "customer not exists"}), 500
    else:
            return jsonify({"message": "Failed to connect to database"}), 500   
                
        
@app.route('/cust/getById', methods=['POST'])
def getCustById():
    conn = connect_db()
    if conn:
            data = request.get_json()
            cust = data.get("ration_id")
            value = 'valid'
            if not cust or (isinstance(cust, str) and not cust.strip()):
                value = 'invalid'
            if value =='valid':
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM customer WHERE ration_id = %s", (cust))
                cust = cursor.fetchone()
                columns = [desc[0] for desc in cursor.description]
                conn.close()
                if cust is None:
                    return  jsonify({"message": "customer not exists or invalid id"}), 500
                else:
                    customer_data = dict(zip(columns, cust))
                    return jsonify(customer_data)
            else:
                return jsonify({"message": "customer not exists or invalid id"}), 500
    else:
            return jsonify({"message": "Failed to connect to database"}), 500  
        
@app.route('/cust/getAll', methods=['GET'])
def getAllCust():
    conn = connect_db()
    if conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM customer")
                customers = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]
                conn.close()
                if not customers:
                    return jsonify({"message": "admin not exists"}), 500
                else:
                    customer_list = [dict(zip(columns, customer)) for customer in customers]
                    return jsonify(customer_list)
    else:
            return jsonify({"message": "Failed to connect to database"}), 500 
@app.route('/product/add', methods=['POST'])
def addProduct():
    conn = connect_db()
    if conn:
        try:
            data = request.get_json()
            store_id = data.get("store_id")
            product_id = data.get("product_id")
            product_name = data.get("product_name")
            unit_of_measure = data.get("unit_of_measure")
            price = data.get("price")
            quantity = data.get("quantity")
            
            # Validate required fields
            if not all([store_id,product_id, product_name, unit_of_measure, price is not None, quantity is not None]):
                return jsonify({"message": "All fields are required"}), 400
                
            # Check if product already exists
            if checkProductExists(product_id):
                return jsonify({"message": "Product ID already exists"}), 400
                
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO product (store_id,product_id, product_name, unit_of_measure, price, quantity) VALUES (%s, %s, %s, %s, %s, %s)",
                (store_id,product_id, product_name, unit_of_measure, price, quantity)
            )
            conn.commit()
            conn.close()
            return jsonify({"message": "Product successfully added"}), 201
        except Exception as e:
            conn.close()
            return jsonify({"message": f"Error adding product: {str(e)}"}), 500
    else:
        return jsonify({"message": "Failed to connect to database"}), 500  
def checkProductExists(productId):
    if not productId or (isinstance(productId, str) and not productId.strip()):
        print("Product ID is empty or invalid")
        return False
    
    conn = connect_db()
    if not conn:
        return False
        
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM product WHERE product_id = %s", (productId,))
        product = cursor.fetchone()
        conn.close()
        return bool(product)  # Returns True if product exists, otherwise False
    except Exception as e:
        print("Database error:", str(e))
        conn.close()
        return False               
@app.route('/product/update', methods=['POST'])
def updateProduct():
    conn = connect_db()
    if conn:
        try:
            data = request.get_json()
            store_id = data.get("store_id")
            product_id = data.get("product_id")
            product_name = data.get("product_name")
            unit_of_measure = data.get("unit_of_measure")
            price = data.get("price")
            quantity = data.get("quantity")
            
            # Validate product ID
            if not product_id:
                return jsonify({"message": "Product ID is required"}), 400
            
            # Check if product exists
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM product WHERE product_id = %s", (product_id,))
            product = cursor.fetchone()
            
            if not product:
                conn.close()
                return jsonify({"message": "Product not found"}), 404
            
            # Update product with all fields
            cursor.execute(
                "UPDATE product SET store_id = %s, product_name = %s, unit_of_measure = %s, price = %s, quantity = %s WHERE product_id = %s",
                (store_id, product_name, unit_of_measure, price, quantity, product_id)
            )
            
            conn.commit()
            conn.close()
            return jsonify({"message": "Product successfully updated"}), 200
            
        except Exception as e:
            if conn:
                conn.close()
            return jsonify({"message": f"Error updating product: {str(e)}"}), 500
    else:
        return jsonify({"message": "Failed to connect to database"}), 500
@app.route('/product/getById', methods=['POST'])
def getProductById():
    conn = connect_db()
    if conn:
        try:
            data = request.get_json()
            product_id = data.get("product_id")
            
            # Validate product ID
            if not product_id or (isinstance(product_id, str) and not product_id.strip()):
                return jsonify({"message": "Product ID is required"}), 400
            
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM product WHERE product_id = %s", (product_id,))
            product = cursor.fetchone()
            
            # Get column names
            columns = [desc[0] for desc in cursor.description]
            conn.close()
            
            if not product:
                return jsonify({"message": "Product not found"}), 404
            
            # Convert to dictionary with column names as keys
            product_data = dict(zip(columns, product))
            return jsonify(product_data), 200
            
        except Exception as e:
            if conn:
                conn.close()
            return jsonify({"message": f"Error retrieving product: {str(e)}"}), 500
    else:
        return jsonify({"message": "Failed to connect to database"}), 500
@app.route('/product/getAll', methods=['GET'])
def getAllProduct():
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM product")
            product = cursor.fetchall()
            
            # Get column names
            columns = [desc[0] for desc in cursor.description]
            conn.close()
            
            if not product:
                return jsonify({"message": "No product found"}), 200
            
            # Convert each product tuple to a dictionary with column names as keys
            product_list = [dict(zip(columns, product)) for product in product]
            return jsonify(product_list), 200
            
        except Exception as e:
            if conn:
                conn.close()
            return jsonify({"message": f"Error retrieving products: {str(e)}"}), 500
    else:
        return jsonify({"message": "Failed to connect to database"}), 500                          
# User Resource (CRUD)
class UserResource(Resource):
    def get(self, user_id=None):
        conn = connect_db()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        if user_id:
            cursor.execute("SELECT * FROM store WHERE village_d = %s", (user_id,))
            user = cursor.fetchone()
            conn.close()
            return jsonify(user) if user else {"message": "User not found"}, 404
        else:
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            conn.close()
            return jsonify(users)

    def post(self):
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        conn.close()

        return {"message": "User created successfully"}, 201

    def put(self, user_id):
        data = request.get_json()
        name = data.get("name")
        email = data.get("email")

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET name=%s, email=%s WHERE id=%s", (name, email, user_id))
        conn.commit()
        conn.close()

        return {"message": "User updated successfully"}

    def delete(self, user_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = %s", (user_id,))
        conn.commit()
        conn.close()

        return {"message": "User deleted successfully"}

# Register API Endpoints
api.add_resource(UserResource, "/users", "/users/<int:user_id>")

if __name__ == "__main__":
    app.run(debug=True)
# Check if product ID already exists
def checkProductExists(productId):
    if not productId or (isinstance(productId, str) and not productId.strip()):
        print("Product ID is empty or invalid")
        return False
    
    conn = connect_db()
    if not conn:
        return False
        
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cursor.execute("SELECT * FROM products WHERE product_id = %s", (productId,))
        product = cursor.fetchone()
        conn.close()
        return bool(product)  # Returns True if product exists, otherwise False
    except Exception as e:
        print("Database error:", str(e))
        conn.close()
        return False
