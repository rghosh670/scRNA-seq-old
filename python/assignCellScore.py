import pandas as pd

cellNames = pd.read_csv('data/t6Stuff/t6.csv',index_col=[0], usecols=[0])
cellNames = cellNames['BWM_anterior:210_270':'BWM_posterior:gt_650']
cellNames = cellNames.index.tolist()
cellScore = pd.DataFrame(index = cellNames)

cellSum = pd.read_csv('data/t6Stuff/sum_t6.csv', index_col=0)
cellSum = cellSum['BWM_anterior:210_270':'BWM_posterior:gt_650']
cellSum = cellSum['sum'].tolist()

for j in range(16):
    f = open('muscle_clusters/cluster' + str(j) + '.txt', 'r')
    genes = f.read().splitlines()
    genes.append('cell')
    f.close()

    eset = pd.read_csv('data/t6Stuff/t6.csv',index_col=[0], header = 0, usecols=genes)
    eset = eset['BWM_anterior:210_270':'BWM_posterior:gt_650']
    sum = eset.sum(axis = 1).tolist()
    scores = []

    for index, value in enumerate(sum):
        scores.append(value/cellSum[index])

    cellScore['cluster' + str(j)] = scores

cellScore.to_csv('muscle_clusters/muscleCellBinScore.csv')
