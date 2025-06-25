from flask import Flask, request, Response
from twilio.twiml.voice_response import VoiceResponse
from intents import parse_intent
from elevenlabs_api import speak
from sheet_utils import log_booking

app = Flask(__name__)

@app.route("/voice", methods=['POST'])
def voice():
    speech_text = request.form.get('SpeechResult', '').lower()
    intent = parse_intent(speech_text)
    response_text = intent.get("response", "I'm sorry, I didn't catch that.")

    audio_url = speak(response_text)
    resp = VoiceResponse()
    resp.play(audio_url)
    return Response(str(resp), mimetype='application/xml')

if __name__ == "__main__":
    app.run(debug=True)