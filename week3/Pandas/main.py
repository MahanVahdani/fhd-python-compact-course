import pandas as pd

df = pd.read_csv("../Data/dataTitanic.csv")

df.set_index("Name", inplace=True)

df.loc[df["Age"] < 18, "Age"] = 18

print(df.isna().sum())

def swap_columns(df, col1, col2):
    columns = list(df.columns)
    i1 = columns.index(col1)
    i2 = columns.index(col2)
    columns[i1], columns[i2] = columns[i2], columns[i1]
    return df[columns]


df = swap_columns(df, "Age", "Fare")

print(df.columns)

df = df[sorted(df.columns)]

print(df.columns)