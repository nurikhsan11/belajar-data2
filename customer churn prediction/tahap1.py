import pandas as pd
df_load = pd.read_csv('https://storage.googleapis.com/dqlab-dataset/dqlab_telco_final.csv')
print(df_load.shape)
print(df_load.head())
print(df_load.customerID.nunique())