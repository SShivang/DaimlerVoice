import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5000')

def runApp():
    while True:
        print('Take input:')
        g = raw_input()
        sio.emit('cust', {'data': g})



print('Hey ho')
runApp()