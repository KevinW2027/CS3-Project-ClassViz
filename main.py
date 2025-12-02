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

plt.figure(figsize=(10,6))

# Use pastel colors for each element
colors = ['#6EB5FF', '#A1E44D', '#FFB347', '#FF6961']

# Create boxplot
bp = plt.boxplot(
    [df[df['Zodiac Element']==elem]['Height Inches'] 
     for elem in df['Zodiac Element'].unique()],
    patch_artist=True,
    labels=df['Zodiac Element'].unique()
)

# Color the boxes
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(0.65)
    patch.set_edgecolor('white')
    patch.set_linewidth(1.8)

# Improve aesthetics
plt.title('Height by Zodiac Element', fontsize=18, fontweight='bold')
plt.xlabel('Zodiac Element', fontsize=14)
plt.ylabel('Height (inches)', fontsize=14)
plt.grid(alpha=0.25)
plt.tight_layout()

plt.savefig('height_by_zodiac.png', bbox_inches='tight')
plt.close()



plt.figure(figsize=(8,6))

plt.scatter(df['States Visited'], df['Countries Visited'], s=80)

# Add labels
for i, row in df.iterrows():
    plt.text(
        row['States Visited'] + 0.1,
        row['Countries Visited'] + 0.1,
        row['Name'],
        fontsize=9
    )

plt.title('States Visited vs Countries Visited', fontsize=16, fontweight='bold')
plt.xlabel('States Visited', fontsize=13)
plt.ylabel('Countries Visited', fontsize=13)
plt.grid(alpha=0.25)
plt.tight_layout()

# Line of best fit
x = df['States Visited'].dropna()
y = df['Countries Visited'].dropna()

m, b = np.polyfit(x, y, 1)   # slope (m) and intercept (b)

# Plot the regression line
plt.plot(x, m * x + b, linewidth=2)

plt.savefig('states_vs_countries.png', bbox_inches='tight')
plt.close()