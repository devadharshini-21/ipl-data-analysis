import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load dataset
df = pd.read_csv('../data/data/matches.csv')
# Top players
players = df['player_of_match'].value_counts().head(10)
print(players)
# Plot chart
plt.figure(figsize=(12,6))
sns.barplot(x=players.index, y=players.values)
plt.xticks(rotation=45)
plt.title('Top Player of the Match Winners')
plt.xlabel('Players')
plt.ylabel('Awards')
plt.tight_layout()
plt.savefig('charts/top_players.png')
plt.show()