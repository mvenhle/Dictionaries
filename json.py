d = {"students": [{"firstName": "Tomas", "lastName": "Shelby"},
                  {"firstName": "Jon", "lastName": "Shelby"},
                  {"firstName": "Auther", "lastName": "Shelby"}],
     "teachers": [{"firstName": "Polly", "lastName": "Gray"},
                  {"firstName": "Micheal", "lastName": "Gray"}]}

print("Original dictionary:")
print(d)
print(type(d))
import json
with open("dictionary", "w") as f:
    json.dump(d, f, indent = 4, sort_keys = True)

print("\nJson file to dictionary:")
with open('dictionary') as f:
    data = json.load(f)
print(data)