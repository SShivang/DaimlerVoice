import socketio
from voiceDriver import runDriver 
sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5000')

def runApp():
        runDriver(sio)


if __name__ == '__main__':
        print('Started app')
        runApp()


#     while True:
#         print('Take input:')
#         g = raw_input()
#         sio.emit('voice', {
#                 'data': g,
#                 'type': 'Voicetype',
        
#         })