import pandas as pd

f = open('data/transcriptionFactors.txt', 'r')
tf = f.read().split()
f.close()


listOfGeneLists = []
for j in range(0,16):
    f = open('wardClusters/cluster' + str(j) + '.txt', 'r')
    geneList = f.read().splitlines()
    f.close()
    listOfGeneLists.append(geneList)

tfCluster = []
for factor in tf:
    found = False
    for geneListIndex, geneList in enumerate(listOfGeneLists):
        if factor in geneList:
            tfCluster.append(geneListIndex)
            found = True
            break

    if not found:
        tfCluster.append(-1)

with open('data/clusterOfTranscriptionFactors.txt', 'w') as f: # write out results to text file
    for item in tfCluster:
        f.write("%s\n" % item)

f.close()