import pandas as pd

df = pd.read_csv("../Data/dataTitanic.csv")

print(df.columns)
print(df.isna().sum())