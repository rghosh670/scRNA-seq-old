import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

genes = pd.read_csv('data/t6Stuff/BWM_t6.csv', index_col=0, skiprows=lambda x: x not in [0]).columns.tolist()

f = open('/home/rohit/Documents/scRNA-seq/data/geneAndTimeData/de_analysis/up_tf.txt', 'r')
up_tf = f.read().splitlines()
f.close()

up_tf_idx = [i+1 for i, val in enumerate(genes) if val in up_tf]

up_tf_idx.insert(0,0)

muscles = ['anterior', 'far_posterior', 'head_row_1', 'head_row_2', 'posterior']
mean_dict = {}

df = pd.DataFrame(columns=up_tf)

for i in muscles:
    temp_df = pd.read_csv('data/geneAndTimeData/bwm_csv/bwm_' + i + '_time_bins.csv', index_col=0, usecols=up_tf_idx)
    df.loc[i] = temp_df.loc['mean'].tolist()

df = df.T
df = df.reindex(df.mean(axis=1).sort_values().index, axis=0)

df.to_csv('data/geneAndTimeData/de_analysis/bwm_up_tf_avg_expression.csv')

# l = []
# for i in range(len(df.index)):
#     for j in range(len(df.columns)):
#         l.append(df.iloc[i,j])
        
# l = np.array(l)
# l = l[(l>np.quantile(l,0.05)) & (l<np.quantile(l,0.95))].tolist()
# l.sort()
# print(l)

ax = sns.heatmap(df, vmin=0, vmax = 30)
plt.show()

plt.savefig('up_tf_heatmap.png')

