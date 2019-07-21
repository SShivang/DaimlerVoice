from voiceDriver import get_intent
from intentGlobals import GO_BACK

def handle_note(sio, response):

    text = response.parameters.fields['note-text'].string_value
    print('Handling note: ', text)
    sio.emit('local', { 'view': 'NOTE', 'action':'', 'noteStr':  text})
    while True:

        response = get_intent(sio)
        if not hasattr(response, 'intent'): continue
        elif response.intent.display_name == GO_BACK:
            sio.emit('local', {'view':'action', 'action':'go_back'})
            return
        else:
            print('writing response')
            sio.emit('local', {'view':'action', 'action':'add_text', 'text': response.query_text})
    sio.emit('local', { 'view': 'NOTE', 'noteStr':  text})
