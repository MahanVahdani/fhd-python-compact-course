import pandas as pd

df = pd.read_csv("../Data/dataTitanic.csv")

average_age = df["Age"].mean()

df["Age"] = df["Age"].fillna(average_age)

print(df["Age"].head())
print("Missing values:", df["Age"].isna().sum())