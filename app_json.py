# app_json.py
import json

siswa = {
    "nama": "Mahmuddin",
    "umur": 20
}

text_json = json.dumps(siswa)
print(text_json)

json_string = '{"nama": "Arya", "umur": 20}'
data_json = json.loads(json_string)
print(data_json.get("nama"))
print(data_json.get("umur"))