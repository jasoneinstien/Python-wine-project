import numpy as np 
import pandas as pd 
from time import time
from IPython.display import display

import matplotlib.pyplot as plt
import seaborn as sns 

#import visuals as vs 

data = pd.read_csv("data/winequality-red.csv" , sep=';')

#check the program normal or not 
#print(data.head())

#check information missing or not 
#print(data.isnull().any())

#seting how many rows 
n_wines =data.shape[0]

#quality above 6 
quality_above_6 = data.loc[(data['quality'] > 6)]
n_above_6 = quality_above_6.shape[0]

#quality from 5 to 6 
quality_between_5 = data.loc[(data['quality'] >= 5) & (data['quality'] <= 6)]
n_between_5 = quality_between_5.shape[0]

#quality below 5 
quality_below_5 = data.loc[(data['quality']) < 5]
n_below_5 = quality_below_5.shape[0]

#precentage above 6
greater_percent = n_above_6*100/n_wines
#print(n_above_6 , n_between_5 , n_below_5)

#data description
#display(np.round(data.describe()))

pd.plotting.scatter_matrix(data, alpha = 0.3, figsize = (40,40), diagonal = 'kde')

correlation = data.corr()
# display(correlation)
plt.figure(figsize=(14, 12))
heatmap = sns.heatmap(correlation, annot=True, linewidths=0, vmin=-1, cmap="RdBu_r")

quality_alcohol = data.loc[(data['quality'] > 0)]

fig, axs = plt.subplots(ncols=1,figsize=(10,6))
sns.barplot(x='quality', y='alcohol', data=quality_alcohol, ax=axs)
plt.title('quality VS alcohol')

plt.tight_layout()
plt.show()
plt.gcf().clear()



