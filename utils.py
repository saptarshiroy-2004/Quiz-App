import json

def load_questions(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data["questions"]
    except FileNotFoundError:
        print("Error: Questions file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return []
