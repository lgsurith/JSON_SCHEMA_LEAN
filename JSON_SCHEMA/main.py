import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

with open(r'C:\Users\lgpoo\OneDrive\Desktop\GSOC_2024\JSON_SCHEMA_LEAN\JSON_SCHEMA\test1.json') as f:
    document = json.load(f)

with open(r'C:\Users\lgpoo\OneDrive\Desktop\GSOC_2024\JSON_SCHEMA_LEAN\JSON_SCHEMA\create_new.json') as f:
    schema = json.load(f)

try:
    validate(instance=document , schema=schema)
    print("Successful Validation")
except ValidationError as e:
    print("Validation Failed!")
    print(f"Error message :{e.message}")
