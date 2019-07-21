from flask import Flask, jsonify, request

@app.route('/twilio')
def home():
    return "<Response> <Say voice=\"alice\">Thanks for trying our documentation. Enjoy!</Say> <Play>http://demo.twilio.com/docs/classic.mp3</Play> </Response>"


    # cur = mysql.connection.cursor()
    # res = cur.execute("SELECT * FROM truckdb.service")
    # mysql.connection.commit()
    # cur.close()
    # print(res)
    # return 'success'





app.run(debug=True, port=8000)
