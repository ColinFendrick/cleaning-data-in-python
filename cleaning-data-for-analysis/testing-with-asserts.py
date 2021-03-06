import pandas as pd

ebola = pd.read_csv('../_datasets/ebola.csv')

# Assert that there are no missing values
assert ebola.notnull().all().all()

# Assert that all values are >= 0
assert (ebola >= 0).all().all()
