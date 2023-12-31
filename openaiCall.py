import requests
import json

# API-Endpunkt und Zugangsschlüssel für OpenAI GPT-4
api_url = "https://api.openai.com/v1/engines/gpt-4/completions"
api_key = "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"

# Daten für den API-Aufruf
data = {
    "prompt": "Übersetze 'Hello, world!' ins Französische.",
    "max_tokens": 60
}

# Header mit dem API-Schlüssel
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# API-Aufruf
response = requests.post(api_url, headers=headers, data=json.dumps(data))

# Antwort verarbeiten
if response.status_code == 200:
    print("Erfolgreiche Antwort:")
    print(response.json())
else:
    print("Fehler bei der Anfrage:")
    print(response.text)