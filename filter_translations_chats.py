import json

keywords = [
    "translate", "translation", "translate to",
    "traducir", "traduce", "översätt",
    "in spanish", "in english", "to spanish", "to english"
]

with open("conversations.json", "r", encoding="utf-8") as f:
    data = json.load(f)

translation_chats = []

for conv in data:
    text = json.dumps(conv).lower()
    if any(k in text for k in keywords):
        translation_chats.append(conv)

with open("translation_chats.json", "w", encoding="utf-8") as f:
    json.dump(translation_chats, f, indent=2)

print("Done. Saved translation_chats.json")
