import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../_datasets/dob_job_application_filings_subset.csv')

df['Existing Zoning Sqft'].plot(kind='hist', rot=70, logx=True, logy=True)

plt.show()
