import json

orig_json_path = open("PATH_TO_JSON.json", 'r')
new_file = open("new_data.json", "w")
NEW_DATA = None

my_json_data = json.load(orig_json_path)

for x in my_data:
    """
    Update NEW_COLUMN and NEW_DATA accordingly
    """
    my_json_data[x]['NEW_COLUMN'] = NEW_DATA
    counter += 1

#Create new json with proper formatting
    #Uses .dumps due to line cutoff issues when using .dump
json_str = json.dumps(my_data, indent = 4)
new_file.write(json_str)
