import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../_datasets/dob_job_application_filings_subset.csv')

# Create and display the first scatter plot
df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()
