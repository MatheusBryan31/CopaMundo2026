import json

with open("Data/Copas/1994.json", encoding="utf-8") as f:
    copa = json.load(f)

for partida in copa["matches"]:
    if partida["round"] == "Final":
        print(partida)