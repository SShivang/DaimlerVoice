from voiceDriver import get_intent, textToSpeech
from intentGlobals import GO_BACK

def handle_note(sio, response):

    text = response.parameters.fields['note-text'].string_value
    print('Handling note: ', text)
    sio.emit('local', { 'view': 'NOTE', 'action':'', 'noteStr':  text})
    textToSpeech('You are currently editing your note. Say go back to exit')
    while True:

        response = get_intent(sio)
        if not hasattr(response, 'intent'): continue
        elif response.intent.display_name == GO_BACK:
            sio.emit('local', {'view':'action', 'action':'go_back'})
            return
        else:
            print('writing response')
            sio.emit('local', {'view':'action', 'action':'add_text', 'text': response.query_text})

def handle_report(sio):
    print('Handling report')
    sio.emit('local', {'view': 'REPORT'})
    textToSpeech('To send the report, say send report. To go back to the diagnostic tool, say go back')

    while True:

        response = get_intent(sio)
        if not hasattr(response, 'intent'): continue
        elif response.intent.display_name == GO_BACK:
            sio.emit('local', {'view':'action', 'action':'go_back'})
            return
        else:
            continue