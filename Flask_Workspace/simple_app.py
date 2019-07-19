

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def index(name=""): 
   # name = request.args.get('name', name)
    return "Oops :/"


#Route For Twillio User Communication 

#...




app.run(debug=True, host='0.0.0.0')


