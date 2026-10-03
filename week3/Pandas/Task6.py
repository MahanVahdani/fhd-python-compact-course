import pandas as pd

df = pd.read_csv("../Data/dataTitanic.csv")

n = int(len(df) * 0.05)

df = df.iloc[n:-n]

print("I removed the first and last 5% of the rows.")
print("Rows left:", len(df))

print("\nHere is the updated data:")
print(df.head())