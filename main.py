import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import flash, request,json
import pprint
from werkzeug import generate_password_hash, check_password_hash

# app = Flask(__name__)

# apply loan api
@app.route("/api/apply_loan",methods=['GET','POST'])
def add_user_loan():
    try:
        user_data = request.json 
        _name= user_data['name']
        _email= user_data['email']
        _address= user_data['address']
        _phone= user_data['phone']
        _salary= user_data['salary']
        _occupation= user_data['occupation']


        create_table='''CREATE TABLE IF NOT EXISTS `user_loan` (
                        `id` int(11) NOT NULL AUTO_INCREMENT,
                        `user_name` varchar(32) DEFAULT NULL,
                        `email` varchar(50) DEFAULT NULL,
                        `address` text,
                        `phone` varchar(16) DEFAULT NULL,
                        `curr_salary` float DEFAULT NULL,
                        `occupation` varchar(32) DEFAULT NULL,
                        `is_approve` varchar(1) DEFAULT NULL,
                        `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
                        `updated_at` datetime DEFAULT NULL,
                        PRIMARY KEY (`id`)
                        ) ENGINE=InnoDB DEFAULT CHARSET=latin1;'''
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(create_table)
        cursor.execute("SELECT * from user_loan where (email=%s ) ",(_email))
        rows = cursor.fetchone()
        print(jsonify(rows))
        if rows!=None:
            resp = jsonify({"msg":"Email already exists"})
            resp.status_code = 302
            return resp
           
        else:
           
            query = "INSERT INTO user_loan(user_name,email,address,phone,curr_salary,occupation) VALUES(%s,%s,%s,%s,%s,%s) "
            bindData = (_name,_email,_address,_phone,_salary,_occupation)
            cursor.execute(create_table)
            cursor.execute(query,bindData)
            conn.commit()
            resp = jsonify({"msg":"Apply loan successfully!"})
            resp.status_code = 201
            return resp
    except Exception as e:
        resp = jsonify({"msg":"Send your data wrong syntax. Please send proper Data1"})
        resp.status_code = 401
        return resp
    finally:
	    cursor.close() 
	    conn.close()

# approve loan
@app.route('/api/approve_loan',methods=['PUT'])
def update_User():
    try:
        data = request.json
        print(data)
        _email = data['email']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * from user_loan where (email=%s ) ",(_email))
        rows = cursor.fetchone()
        print("======",rows)
        if rows!=None:
            approve_query  = "Update user_loan set is_approve='Y',updated_at=now() where email =%s"
            cursor.execute(approve_query,_email)
            conn.commit()
            resp = jsonify({"msg":'Approve Loan successfully!'})
            resp.status_code = 200
            return resp
        else:
            resp = jsonify({"msg":"Email does not exists"})
            resp.status_code = 302
            return resp
    except  Exception as e:
        resp = jsonify({"msg":"Send your data wrong syntax. Please send proper Data"})
        resp.status_code = 401
        return resp
    finally:
	    cursor.close() 
	    conn.close()

# user loan apply but not approve
@app.route('/api/getUserLoanApply',methods=['GET'])
def getUser():
    try:
        conn = mysql.connect()

        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT user_name,email,address,phone,curr_salary,occupation  FROM user_loan  ORDER BY id ")
        rows = cursor.fetchall()
        resp  = jsonify({"ApplyLoan":rows,"toltaluser":len(rows)})
        resp.status_code = 200
        return resp
    except Exception:
        resp = jsonify({"msg":"Data not found"})
        resp.status_code = 401
        return resp
    finally:
        conn.close()
        cursor.close()
    

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Sorry API Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run(debug=True)
    app.run()
