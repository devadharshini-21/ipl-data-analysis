import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load dataset
df = pd.read_csv('../data/data/matches.csv')
# Team wins count
team_wins = df['winner'].value_counts()
print(team_wins)
# Plot chart
plt.figure(figsize=(12,6))
sns.barplot(x=team_wins.index, y=team_wins.values)
plt.xticks(rotation=90)
plt.title('IPL Match Wins by Team')
plt.xlabel('Teams')
plt.ylabel('Wins')
plt.tight_layout()
plt.savefig('charts/top_teams.png')
plt.show()