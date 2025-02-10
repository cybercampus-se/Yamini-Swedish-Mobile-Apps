import json

with open("testSL.json", "r", encoding="utf-8") as file:
    try:
        data = json.load(file)
        print("✅ JSON is valid!")
    except json.JSONDecodeError as e:
        print(f"❌ JSON Error: {e}")
