import assemblyai as aai
from dotenv import *
import requests
import io
import os
import time

load_dotenv()
api_key = os.getenv("ASSEMBLYAI_API_KEY")
base_url = "https://api.assemblyai.com/v2"
headers = {
    "authorization": api_key
}

def transcribe(audio):
    audio_file = io.BytesIO(audio)
    upload_response = requests.post(
        base_url + "/upload",
        headers = headers,
        data = audio_file
    )
    print("Upload status:", upload_response.status_code)
    print("Upload response text:", upload_response.text)
    if upload_response.status_code != 200:
        raise RuntimeError(f"Upload failed: {upload_response.text}")

    upload_url = upload_response.json()["upload_url"]
    transcript_request = {
        "audio_url": upload_url,
        "language_detection": True,
        "speech_models": ["universal-3-pro", "universal-2"]
    }
    transcript_response = requests.post(
        base_url + "/transcript",
        json=transcript_request,
        headers=headers
    )
    transcript_id = transcript_response.json()["id"]
    polling_endpoint = base_url + "/transcript/" + transcript_id
    while True:
        result = requests.get(polling_endpoint, headers=headers).json()
        if result["status"] == "completed":
            return result["text"]
        elif result["status"] == "error":
            raise RuntimeError(f"Transcription failed: {result['error']}")
        else:
            time.sleep(3)