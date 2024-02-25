import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

#give your file to be tested as a json.
with open(r'C:\Users\Edith\OneDrive\Desktop\GSOC_2024\JSON_SCHEMA_LEAN\JSON_SCHEMA\test1.json') as f:
    document = json.load(f)

#give your path for the json schema used to validate the json.
with open(r'C:\Users\Edith\OneDrive\Desktop\GSOC_2024\JSON_SCHEMA_LEAN\JSON_SCHEMA\create_new.json') as f:
    schema = json.load(f)

try:
    validate(instance=document , schema=schema)
    print("Successful Validation")
except ValidationError as e:
    print("Validation Failed!")
    print(f"Error message :{e.message}")
