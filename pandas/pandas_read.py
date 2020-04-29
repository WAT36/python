import pandas as pd
df = pd.read_csv('read_sample.csv')

print(df)
print(df['index'][0])
print(df['name'][1])
print(df['yen'][2])