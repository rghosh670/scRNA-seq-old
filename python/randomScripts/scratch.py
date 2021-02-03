from scipy import stats

x = [30, 31, 32, 33, 34]
y = [0, 1, 2 ,3 ,4]

correlation, p_value = stats.pearsonr(x, y)

print(correlation)