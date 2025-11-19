# dictionary_json_usage.py
import json

data = {"name": "Sanjog", "age": 18, "skills": ["Python", "ML", "AI"]}

json_string = json.dumps(data)   # dict → JSON string
print("JSON String:", json_string)

dict_data = json.loads(json_string)  # JSON → dict
print("Dictionary again:", dict_data)
