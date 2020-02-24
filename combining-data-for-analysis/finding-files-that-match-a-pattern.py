import glob
import pandas as pd

pattern = '**/*.csv'

# Save all file matches: csv_files
csv_files = glob.glob(pattern)

# Print the file names
print(csv_files)

csv2 = pd.read_csv(csv_files[1])

print(csv2.head())
