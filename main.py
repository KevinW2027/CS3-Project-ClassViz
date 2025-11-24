import pandas as pd 
import numpy as np
from matplotlib import pyplot as plt

# set style theme
plt.style.use('dark_background')

#read csv into dataframe
df = pd.read_csv('ClassDataset.csv')
df = df.head(8)
print(df.info)

# Group by neighborhood and compute the average
avg_df = df.groupby('Neighborhood')['Commute Time Minutes'].mean()
plt.bar(avg_df.index,avg_df.values, width= 0.6)

plt.xlabel('Neighborhood')
plt.ylabel('Commute time Minutes')
plt.savefig('barchart.png', bbox_inches='tight')
plt.close()