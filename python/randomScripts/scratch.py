import pandas as pd

f = open('data/muscleTFStuff/listOfTFsNotInClusters.txt', 'r')
tf = f.read().splitlines()
f.close()

col = pd.read_csv('data/t6Stuff/mean_t6.csv', index_col=[0])['ets-8'].tolist()
print(col)