from flask import Flask, jsonify, request
<<<<<<< HEAD
from flaskext.mysql import MySQL
import mysql.connector
from twilio.rest import Client



app = Flask(__name__)
mysql = MySQL()


app.config['MYSQL_DATABASE_USER'] = 'sql9299267'
app.config['MYSQL_DATABASE_PASSWORD'] = 'sHDDIRT8R8'
app.config['MYSQL_DATABASE_DB'] = 'sql9299267'
app.config['MYSQL_DATABASE_HOST'] = 'sql9.freemysqlhosting.net'


mysql.init_app(app)

con = mysql.connect()


def findPhoneByCustomer(customer_id="1"): 
    phoneNumber = select("phone", "customer", "cusomter_id", customer_id)
    print(phoneNumber)
    makeCall(phoneNumber)
    print("Call Initiated")



def select(attribute, table, value="",query=""):
    cur = mysql.get_db().cursor()
    if query == "":
        res = cur.execute("SELECT {} FROM sql9299267.{}".format(attribute, table))
    else: 
        res = cur.execute("SELECT {} FROM sql9299267.{} where {}={}".format(attribute, table, query, value))
    con.commit()
    data = cur.fetchall()
    cur.close
    return data
=======
>>>>>>> presentation

@app.route('/twilio')
def home():
    return "<Response> <Say voice=\"alice\">Thanks for trying our documentation. Enjoy!</Say> <Play>http://demo.twilio.com/docs/classic.mp3</Play> </Response>"

<<<<<<< HEAD
@app.route('/')
def home():
    findPhoneByCustomer()
    return "OK 200"

@app.route('/diagnostic/<int:id>', methods=['GET', 'POST', 'DELETE','PUT'])
def diagnostic(id): 
    if request.method == "GET":
        data = select("*", "customer", "customer_id", 1)
        return jsonify(data)
   
    return "BOOO :("

@app.route('/diagnostic')
def diagnostics():
    data = select("*", "customer")
    makeCall()
    return jsonify(data)
   
    
=======

>>>>>>> presentation
    # cur = mysql.connection.cursor()
    # res = cur.execute("SELECT * FROM sql9299267.customer")
    # mysql.connection.commit()
    # cur.close()
    # print(res)
    # return 'success'


def makeCall(phoneNumber="3057854963"):
    account_sid = 'AC9d73877c3494c64be0e863b8f0c63fef'
    auth_token = 'eac4bd1897c29a0d4e1921fecf8809b1'
    client = Client(account_sid, auth_token)

    call = client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml',
        to=phoneNumber,
        from_='+19545161885'
                    )
    print(call.sid)

def sendText(phoneNumber="3057854963"):
    account_sid = 'AC9d73877c3494c64be0e863b8f0c63fef'
    auth_token = 'eac4bd1897c29a0d4e1921fecf8809b1'
    client = Client(account_sid, auth_token)

    message = client.messages \
                .create(
                     body="Daimler Truck: Approve Transaction 1249, $1,200.00",
                     from_='+19545161885',
                     to=phoneNumber
                 )

    print(message.sid)



app.run(debug=True, port=8000)

