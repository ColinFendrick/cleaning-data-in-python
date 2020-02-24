import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../_datasets/dob_job_application_filings_subset.csv')

df.boxplot(column='initial_cost', by='Borough', rot=90)
plt.show()
