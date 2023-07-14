import json

def main():
    new_path = input("enter path to new file: ")

    with open(new_path, "r") as new_file:
        new = json.load(new_file)

    old_path = input("enter path to old file: ")

    with open(old_path, "r") as old_file:
        old = json.load(old_file)

    combined = {
        "stats": {},
        "DataVersion": new["DataVersion"]
    }

    for category in new["stats"]:
        combined["stats"][category] = {}

        for stat in new["stats"][category]:

            if stat in old["stats"][category]:
                combined["stats"][category][stat] = new["stats"][category][stat] + old["stats"][category][stat]
            else:
                combined["stats"][category][stat] = new["stats"][category][stat]

    for category in old["stats"]:
        for stat in old["stats"][category]:
            if stat not in combined["stats"][category]:
                combined["stats"][category][stat] = old["stats"][category][stat]
    
    for category in combined["stats"]:
        for stat in combined["stats"][category]:
            if stat in new["stats"][category] and stat in old["stats"][category]:
                if combined["stats"][category][stat] == new["stats"][category][stat] + old["stats"][category][stat]:
                    print("correct! ✅")
                else:
                    print("wrong! ❌")
            elif stat in new["stats"][category]:
                if combined["stats"][category][stat] == new["stats"][category][stat]:
                    print("correct! ✅")
                else:
                    print("wrong! ❌")
            elif stat in old["stats"][category]:
                if combined["stats"][category][stat] == old["stats"][category][stat]:
                    print("correct! ✅")
                else:
                    print("wrong! ❌")

    with open("UUID.json", "w") as combined_file:
        json.dump(combined,combined_file)

main()