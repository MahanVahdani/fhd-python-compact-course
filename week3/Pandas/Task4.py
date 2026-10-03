import pandas as pd

df = pd.read_csv("../Data/dataTitanic.csv")

print("These are the columns in the DataFrame:")
print(df.columns)

print("\nHere is how many values are missing in each column:")
print(df.isna().sum())