import pandas as pd

df = pd.read_csv("../Data/dataTitanic.csv")

df.set_index("Name", inplace=True)

print(df.head())