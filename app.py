import os
from pathlib import Path

import requests
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from werkzeug.utils import secure_filename


load_dotenv()

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB

GNANI_STT_URL = "https://api.vachana.ai/stt/v3"
ALLOWED_EXTENSIONS = {"wav", "mp3", "ogg", "flac", "aac", "m4a"}


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.get("/")
def home():
    return render_template("index.html")


@app.post("/transcribe")
def transcribe():
    api_key = os.getenv("GNANI_API_KEY")
    if not api_key:
        return jsonify(error="The app is not configured yet. Add GNANI_API_KEY to your local .env file."), 500

    audio = request.files.get("audio")
    if not audio or not audio.filename:
        return jsonify(error="Choose an audio file first."), 400
    if not allowed_file(audio.filename):
        return jsonify(error="Use WAV, MP3, OGG, FLAC, AAC, or M4A audio."), 400

    filename = secure_filename(audio.filename)
    files = {"audio_file": (filename, audio.stream, audio.mimetype or "application/octet-stream")}
    data = {
        "model": "prisma-v3.0",
        "language_code": "te-IN,en-IN",
        "format": "codemix",
        "topic": "A cyber fraud incident report described in Telugu.",
        "keyterms": '["OTP", "UPI", "1930", "Aadhaar", "WhatsApp", "bank"]',
    }

    try:
        response = requests.post(
            GNANI_STT_URL,
            headers={"X-API-Key-ID": api_key},
            files=files,
            data=data,
            timeout=55,
        )
    except requests.Timeout:
        return jsonify(error="Gnani took too long to respond. Please try a shorter audio clip."), 504
    except requests.RequestException:
        return jsonify(error="Could not reach Gnani right now. Check your internet and try again."), 503

    try:
        result = response.json()
    except ValueError:
        return jsonify(error="Gnani returned an unexpected response. Please try again."), 502

    if not response.ok:
        message = result.get("error", {}).get("message") or result.get("message") or "Transcription failed."
        return jsonify(error=message), response.status_code

    transcript = result.get("transcript")
    if not transcript:
        return jsonify(error="Gnani did not return usable text from this clip. Try a clearer recording under 30 seconds, or type the incident description manually below."), 502

    return jsonify(
        transcript=transcript,
        detected_language=result.get("detected_language_code", "Not reported"),
        model=result.get("model", "prisma-v3.0"),
    )


@app.errorhandler(413)
def file_too_large(_error):
    return jsonify(error="That file is too large. Choose an audio file smaller than 10 MB."), 413


if __name__ == "__main__":
    app.run(debug=True)
