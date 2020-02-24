import pandas as pd
import glob

frames = []
csv_files = glob.glob('**/*.csv')

#  Iterate over csv_files
for csv in csv_files:
    #  Read csv into a DataFrame: df
    df = pd.read_csv(csv)

    # Append df to frames
    frames.append(df)

# Concatenate frames into a single DataFrame: uber
uber = pd.concat(frames)

print(uber.shape)

print(uber.head())
