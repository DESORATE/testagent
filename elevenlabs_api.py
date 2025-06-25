import os
import requests

def speak(text):
    api_key = os.getenv("ELEVENLABS_API_KEY")
    voice_id = os.getenv("ELEVENLABS_VOICE_ID")

    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}/stream"

    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }

    payload = {
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }

    try:
        os.makedirs("static", exist_ok=True)
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        with open("static/response.mp3", "wb") as f:
            f.write(response.content)

        print("response.mp3 saved successfully")
        return "https://testagent-eb2i.onrender.com/static/response.mp3"

    except Exception as e:
        print(f"Error generating voice: {e}")
        return "https://testagent-eb2i.onrender.com/static/fallback.mp3"
