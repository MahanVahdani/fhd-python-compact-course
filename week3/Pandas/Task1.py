import pandas as pd

df = pd.read_csv("../Data/dataTitanic.csv")

print("Here is a quick look at the Titanic data:")
print(df.head())