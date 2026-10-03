import pandas as pd

data1 = {
    "ID": [1, 2, 3],
    "Name": ["Mahan", "Sara", "Mohsen"]
}

data2 = {
    "ID": [1, 2, 3],
    "Age": [28, 25, 30]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

merged = pd.merge(df1, df2, on="ID")

print(merged)

result = pd.concat([df1, df2[["Age"]]], axis=1)

print(result)