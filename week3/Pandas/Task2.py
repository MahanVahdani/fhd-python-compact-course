import pandas as pd

df = pd.read_csv("../Data/dataTitanic.csv")

df.set_index("Name", inplace=True)

print("I set the passenger names as the DataFrame index:")
print(df.head())