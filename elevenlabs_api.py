import os
import requests

def speak(text):
    api_key = os.getenv("ELEVENLABS_API_KEY")
    voice_id = os.getenv("ELEVENLABS_VOICE_ID", "rachel")
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json"
    }
    data = {
        "text": text,
        "voice_settings": {"stability": 0.75, "similarity_boost": 0.75}
    }

    os.makedirs("static", exist_ok=True)  # <--- ensures folder exists
    response = requests.post(url, headers=headers, json=data)
    with open("static/response.mp3", "wb") as f:
        f.write(response.content)

    return "https://your-app-name.onrender.com/static/response.mp3"
