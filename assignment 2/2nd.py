#For this assignment, let’s use example 5. Store the example 5 json in a file ex5.json.
#Read the json using python, store in a dictionary named ex5
#Write a code to add a batter named Coffee for “donut” with name “Old Fashoined”.
#Replace the ex5.json with the new data.


import json

with open('ex5.json') as json_file:
    ex5 = json.load(json_file)
    ex5[2]['batters']['batter'].append({'id': '1003', 'type': 'Coffee'})
    print(ex5)


with open('ex5.json','w') as json_file:
    json.dump(ex5,json_file,indent=2)
