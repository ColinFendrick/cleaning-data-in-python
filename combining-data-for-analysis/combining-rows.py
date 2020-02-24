import pandas as pd

uber1 = pd.read_csv('../_datasets/nyc_uber_2014.csv')
uber2 = pd.read_csv('../_datasets/nyc_uber_2014.csv')
uber3 = pd.read_csv('../_datasets/nyc_uber_2014.csv')
row_concat = pd.concat([uber1, uber2, uber3])

print(row_concat.shape)

print(row_concat.head())
