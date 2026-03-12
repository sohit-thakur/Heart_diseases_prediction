import pandas as pd

df = pd.read_csv('Heart_new2.csv')


print(df.head())
print(df.info())
print(df.describe(include='all'))