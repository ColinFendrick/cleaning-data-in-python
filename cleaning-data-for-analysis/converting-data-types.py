import pandas as pd

tips = pd.read_csv('../_datasets/tips.csv')

# Convert the sex column to type 'category'
tips.sex = tips.sex.astype('category')

# Convert the smoker column to type 'category'
tips.smoker = tips.smoker.astype('category')

print(tips.info())
