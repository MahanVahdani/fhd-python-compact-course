import pandas as pd

df = pd.read_csv("../Data/dataTitanic.csv")

n = int(len(df) * 0.05)

df = df.iloc[n:-n]

print(df.head())
print("Rows:", len(df))