from flask import  Flask  , request , jsonify
import sqlite3
import pymongo
from pymongo import MongoClient
app =  Flask(__name__)

# to reach out we have to create route
# @act as decorator
@app.route('/xyz',methods = ['GET','POST'])
def test():
    if(request.method == 'POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a + b
        return jsonify(str(result))

@app.route('/sql', methods = ['GET','POST'])
def sql_fetch():
    conn = sqlite3.connect('C:\\Users\\anilk\\Documents\\api.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify({'data': rows})

@app.route('/mongo' , methods = ['GET','POST'])
def mongo_fetch():
    try:
        client = MongoClient("mongodb+srv://mongo:mongo@cluster0.ubeiz69.mongodb.net/test?retryWrites=true&w=majority")
        db = client.test
        db2 = client["AnilKAMAT"]
        document1 = db2["My_DATA"]
        data1 = list(document1.find())
        for doc in data1:
            doc['_id'] = str(doc['_id'])
        # Convert cursor to list of documents
        client.close()
        return jsonify({'data': data1})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
#GET AND POST botSEND DATA TO REFERENCE SYSTEM, BUT IN  different way
# in get our data we are sending is exposed but in post data we are sending is not exposed
if __name__ == '__main__':
    app.run() #this will keep my server uo running

#this is constructor call of python main function

# Task 1 : write a function to fetch data from sql table via api
# task 2 : write a function to fetch a data from mongodb table