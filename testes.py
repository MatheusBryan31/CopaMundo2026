import json

with open("Data/Copas/1994.json", encoding="utf-8") as f:
    copa = json.load(f)

print("Nome da copa:", copa["name"])

print("\n===== PARTIDAS COM ROUND 'Final' =====")

for partida in copa["matches"]:
    if partida["round"] == "Final":
        print(partida)