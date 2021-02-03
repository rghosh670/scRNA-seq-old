import json

with open('data/muscleTFStuff/muscleClusterDict.txt') as json_file:
    x = json.load(json_file)
json_file.close()

with open('data/muscleTFStuff/tfClusterDict.txt') as json_file:
    y = json.load(json_file)
json_file.close()
