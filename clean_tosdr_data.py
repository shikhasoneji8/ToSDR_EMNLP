import pandas as pd
import re

def clean_html(text):
    html = re.compile('<.*?>')  # regex
    return html.sub(r'', text)

# Read the data from the csv
df = pd.read_csv('filtered_data_colab.csv')

# Remove non-ASCII characters from the 'Description' column
df['Description'] = df['Description'].apply(lambda x: re.sub(r'[^\x00-\x7F]+',' ', x))

# Remove the last two lines from each 'Description'
df['Description'] = df['Description'].apply(lambda x: '\n'.join(x.split('\n')[:-2]) if isinstance(x, str) else x)

# Remove html tags from 'Description'
df['Description'] = df['Description'].apply(lambda x: clean_html(x) if isinstance(x, str) else x)


df['Case'] = df['Case'].apply(lambda x: re.sub(r'[^\x00-\x7F]+',' ', x))


# Write the data back to the csv
df.to_csv('filtered_data_colab_clean.csv', index=False)
