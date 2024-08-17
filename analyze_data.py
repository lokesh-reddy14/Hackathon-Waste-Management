import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('items.csv')

print("Data Overview:")
print(df.info())
print("\nFirst few rows of the dataset:")
print(df.head())

category_counts = df['category'].value_counts()

plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Items by Category')
plt.xlabel('Category')
plt.ylabel('Number of Items')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('category_distribution.png')
plt.show()

df['replacement_date'] = pd.to_datetime(df['replacement_date'])
items_needing_replacement = df[df['replacement_date'] < pd.Timestamp.now()]

print("\nItems Needing Replacement:")
print(items_needing_replacement)

items_needing_replacement.to_csv('items_needing_replacement.csv', index=False)
