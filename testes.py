import json

with open("Data/Copas/1950.json", encoding="utf-8") as f:
    copa = json.load(f)

for partida in copa["matches"]:
    print(partida["round"])