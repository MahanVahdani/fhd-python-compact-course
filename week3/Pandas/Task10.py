import pandas as pd

df = pd.read_csv("../Data/dataTitanic.csv")

print(df[["Age", "Survived", "Pclass", "SibSp", "Parch", "Fare"]].corr())