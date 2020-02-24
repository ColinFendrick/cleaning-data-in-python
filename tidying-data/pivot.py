import pandas as pd

airquality = pd.read_csv('../_datasets/airquality.csv')

airquality_melt = pd.melt(frame=airquality, id_vars=[
                          'Month', 'Day'], var_name='measurement', value_name='reading')

print(airquality_melt.head())

# Pivot airquality_melt: airquality_pivot
airquality_pivot = airquality_melt.pivot_table(
    index=['Month', 'Day'], columns='measurement', values='reading')

print(airquality_pivot.head())
