import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv('../data/data/matches.csv')
# Toss winner analysis
toss = df['toss_winner'].value_counts().head(10)
print(toss)
# Chart
plt.figure(figsize=(12,6))
toss.plot(kind='bar')
plt.title('Top Toss Winning Teams')
plt.xlabel('Teams')
plt.ylabel('Toss Wins')
plt.tight_layout()
plt.savefig('charts/toss_impact.png')
plt.show()