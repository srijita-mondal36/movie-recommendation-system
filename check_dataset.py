import pandas as pd

df = pd.read_csv("movies_dataset.csv")

print("Columns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())