import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv('../data/data/matches.csv')
# City analysis
cities = df['city'].value_counts().head(10)
print(cities)
# Chart
plt.figure(figsize=(12,6))
cities.plot(kind='barh')
plt.title('Top IPL Host Cities')
plt.xlabel('Matches')
plt.ylabel('City')
plt.tight_layout()
plt.savefig('charts/city_matches.png')
plt.show()
