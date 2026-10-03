import pandas as pd

df = pd.read_csv("../Data/dataTitanic.csv")

df.set_index("Name", inplace=True)

df.loc[df["Age"] < 18, "Age"] = 18

print(df.columns)
print(df.isna().sum())