import json
import csv 

file_data = open("process.json","r")
rows = []
filename = "university_records.csv"

for raw_json in file_data:
  person_dict = json.loads(raw_json)
  new_json = {}
  new_json['branch'] = person_dict['branch']
  new_json['commit'] = person_dict['commit']
  new_json['reason'] = person_dict['reason']
  new_json['stringsFound'] = person_dict['stringsFound']
  new_json['path'] = person_dict['path']
  rows.append(new_json)

fields = ["branch","commit","reason","stringsFound","path"]
with open(filename, 'w') as csvfile: 
    # creating a csv dict writer object 
    writer = csv.DictWriter(csvfile, fieldnames = fields) 
        
    # writing headers (field names) 
    writer.writeheader() 
        
    # writing data rows 
    writer.writerows(rows)
