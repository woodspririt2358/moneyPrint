import openai

# Setze deine API-Schlüssel hier ein
api_key = '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'
openai.api_key = api_key

# Deine Anfrage an die API
prompt_text = "Wie kann ich dir helfen?"

# Beispielhaftes GPT-3.5 Modell
model = "text-davinci-003"

# Die Anfrage an die API senden
response = openai.Completion.create(
  engine=model,
  prompt=prompt_text,
  max_tokens=50  # Anzahl der zurückgegebenen Tokens (max. 2048)
)

# Die Antwort der API als String ausgeben
print(response.choices[0].text.strip())
