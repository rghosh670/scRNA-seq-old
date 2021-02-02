import scipy
from scipy.cluster.hierarchy import fcluster
from scipy import stats
import scipy.cluster.hierarchy as hac
import statistics
from statistics import mode
from math import floor
import random
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import matplotlib
from cellNames import getCellName
import datetime

TOTAL_NUM_CELLS = 37148

cellList = []
for i in range(TOTAL_NUM_CELLS):
    cellList.append(getCellName(i))

userCell = input('Enter cell name: ').strip()

if userCell =='all_cells':
    rowList = [*range(1, TOTAL_NUM_CELLS+1)]
elif userCell == 'muscle_cells':
    rowList = [i + 1 for i, value in enumerate(cellList) if ('BWM' in value)]
else:
    rowList = [i + 1 for i, value in enumerate(cellList) if (value == userCell or userCell in value and type(value) is tuple)]

rowList.insert(0, 0)

if not rowList:
    print('Not a valid cell')
    exit()

f = open('data/geneAndTimeData/usefulTimes.txt', 'r')
timeList = f.read().splitlines()
timeList = [timeList[i-1] for i in rowList[1:]]
f.close()

f = open('data/geneAndTimeData/listOfGenes.txt', 'r')
geneList = f.read().splitlines()
f.close()

eset = pd.read_csv('data/geneAndTimeData/rawReads.csv', index_col = None, skiprows = lambda x : x not in rowList, header = 0)
timeListWithoutDuplicates = list(dict.fromkeys(timeList))

df = pd.DataFrame(index=geneList,
                  columns=timeListWithoutDuplicates)
df = df.fillna(1e-10)

for row, expressionSeries in eset.iterrows():
    for i in range(len(expressionSeries.index)):
        if expressionSeries.values[i] != 0.0:
            if df.at[expressionSeries.index[i], timeList[row]] == 1e-10:
                try:
                    df.at[expressionSeries.index[i], timeList[row]] = expressionSeries.values[i]
                except:
                    print(expressionSeries.index[i], timeList[row])
            else:
                df.at[expressionSeries.index[i], timeList[row]] = (expressionSeries.values[i] + df.at[expressionSeries.index[i], timeList[row]])/2

df = df.reindex(sorted(df.columns), axis=1)

df = df[(df.T != 1e-10).any()]

def my_metric(x, y):
    r = stats.pearsonr(x, y)[0]
    return 1 - r  # correlation to distance: range 0 to 2


def findDistanceMatrix():
    dist = scipy.spatial.distance.pdist(df, metric=my_metric)
    np.savetxt('muscle_dist.csv', dist, delimiter=',')
    return

findDistanceMatrix()

def dendrogram(plot):
    Z = hac.linkage(df,  method='single', metric=my_metric)
    np.savetxt('muscle_linkage.csv', Z, delimiter = ',')

    plt.figure(figsize=(12.5, 5))
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('sample index')
    plt.ylabel('distance')
    hac.dendrogram(
        Z,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels
    )
    if plot:
        plt.show()
        plt.savefig('muscle_ward_dendrogram.png')
    return Z
# Z = dendrogram(plot=True)

def print_clusters(timeSeries, Z, k, plot=False):
    # k Number of clusters I'd like to extract
    results = fcluster(Z, k, criterion='maxclust')

    # check the results
    s = pd.Series(results)
    clusters = s.unique()

    for c in clusters:
        cluster_indeces = s[s == c].index
        print(cluster_indeces)
        if plot:
            timeSeries.T.iloc[:, cluster_indeces].plot()
            plt.show()
    return
# print_clusters(df, Z, 60, plot=False)
