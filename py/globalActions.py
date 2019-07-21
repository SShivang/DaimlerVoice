def handle_note(sio, response):
    text = response.parameters.fields['note-text'].string_value
    print('Handling note: ', text)
    sio.emit('local', { 'view': 'NOTE', 'noteStr':  text})
