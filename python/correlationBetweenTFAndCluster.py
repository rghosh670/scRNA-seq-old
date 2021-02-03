import pandas as pd
from listOfIndicesFromGenes import get_indices

f = open('data/muscleTFStuff/transcriptionFactors.txt', 'r')
tf = f.read().splitlines()
f.close()

tf_indices = get_indices(tf)
tf_indices.append(0)

t6 = pd.read_csv('data/t6Stuff/t6.csv', index_col = 0, usecols=tf_indices)
t6 = t6['BWM_anterior:210_270':'BWM_posterior:gt_650']

cellScore = pd.read_csv('wardClusters/wardCellBinScore.csv', index_col=0)
cellScore = cellScore['BWM_anterior:210_270':'BWM_posterior:gt_650']
print(cellScore)
