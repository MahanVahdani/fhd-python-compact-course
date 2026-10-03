import pandas as pd

df = pd.read_csv("../Data/dataTitanic.csv")

df.loc[df["Age"] < 18, "Age"] = 18

print(df[["Name", "Age"]].head())