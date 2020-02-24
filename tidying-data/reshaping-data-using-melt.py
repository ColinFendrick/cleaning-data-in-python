import pandas as pd

airquality = pd.read_csv('../_datasets/airquality.csv')

print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(frame=airquality, id_vars=['Month', 'Day'])

print(airquality_melt.head())
