from flask import Flask
from twilio.twiml.voice_response import VoiceResponse, Say

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def answer_call():
    """Respond to incoming phone calls with a brief message."""
    # Start our TwiML response
    resp = VoiceResponse()

    print("dsadhsajdhsajdhaskdhaskh")
    # Read a message aloud to the caller
    resp.say("We need your approval for a engine part not under warranty. Please contact us again as soon as possible", voice='alice')

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
