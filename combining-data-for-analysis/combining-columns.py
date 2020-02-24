import pandas as pd

ebola = pd.read_csv('../_datasets/ebola.csv')

ebola_melt = pd.melt(
    ebola, id_vars=['Date', 'Day'], var_name='type_country', value_name='counts')

ebola_tidy = pd.concat([ebola_melt], axis=1)

# Print the shape of ebola_tidy
print(ebola_tidy.shape)

# Print the head of ebola_tidy
print(ebola_tidy.head())