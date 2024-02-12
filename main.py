import pandas as pd

df = pd.read_csv('amazon-orders.csv')
df.head()

data_size = df.shape

print(data_size)
