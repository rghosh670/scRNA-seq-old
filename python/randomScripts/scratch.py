import json
import collections

with open('data/muscleTFStuff/muscleClusterDict.txt') as json_file:
    mcDict = json.load(json_file)
json_file.close()

od = collections.OrderedDict(sorted(mcDict.items()))
mcDict = dict(od)


with open('data/muscleTFStuff/muscleClusterDict.txt', 'w') as outfile:
    json.dump(mcDict, outfile)
outfile.close()
