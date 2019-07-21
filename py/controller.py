from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
import mysql.connector

app = Flask(__name__)


mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'clock123'
app.config['MYSQL_DATABASE_DB'] = 'truckdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'


mysql.init_app(app)

con = mysql.connect()


def select(attribute, table, value="",query=""):
    cur = mysql.get_db().cursor()
    if query == "":
        res = cur.execute("SELECT {} FROM truckdb.{}".format(attribute, table))
    else: 
        res = cur.execute("SELECT {} FROM truckdb.{} where {}={}".format(attribute, table, query, value))
    con.commit()
    data = cur.fetchall()
    cur.close
    return data


@app.route('/diagnostic/<int:id>', methods=['GET', 'POST', 'DELETE','PUT'])
def serviceRequest(id): 
    if request.method == "GET":
        data = select("*", "diagnostic", "diagnostic_id", 1)
        return jsonify(data)
   
    return "BOOO :("

@app.route('/diagnostic')
def home():
    data = select("*", "diagnostic")
    return jsonify(data)
   
    
    # cur = mysql.connection.cursor()
    # res = cur.execute("SELECT * FROM truckdb.service")
    # mysql.connection.commit()
    # cur.close()
    # print(res)
    # return 'success'





app.run(debug=True, port=8000)
