import json

data_folder = input("Path for the folder where the file is located: ")

file_name = input("Name of the file with extensions: ")

file_to_open = data_folder + file_name

with open(file_to_open) as files:
    file=files.read()

obj = json.loads(file)

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
    
jprint(obj)

files.close()
