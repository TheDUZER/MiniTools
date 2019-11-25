import json, pandas

orig_json_path = open("PATH_TO_JSON.json", 'r')
csv_path = open("PATH_TO_CSV.csv", 'r')
new_file = open("new_data.json", "w")

my_json_data = json.load(orig_json_path)
my_csv_data = pandas.read_csv(csv_path)

counter = 0

for x in my_data:
    '''
    This specific situation involved adding a new column of data
    which was mistakenly omitted when the original json file was created.
    As such, this loop assumes a 1:1 relationship between the lengths of each
    file.
    '''
    my_json_data[x]['NEW_COLUMN'] = my_new_data.imageFileName[counter]
    counter += 1

#Create new json with proper formatting
json.dump(my_data, new_file, indent = 4)
