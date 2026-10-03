import pandas as pd
import numpy as np

df = pd.read_csv("../Data/dataTitanic.csv")

counts, bins = np.histogram(df["Age"].dropna())

print("Bins:", bins)
print("Counts:", counts)