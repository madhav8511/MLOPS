import pandas as pd

df = pd.read_csv("data/raw/iris.csv")

# Example cleaning (for learning)
df = df.dropna()

df.to_csv("data/processed.csv", index=False)

print("Data cleaning completed!")