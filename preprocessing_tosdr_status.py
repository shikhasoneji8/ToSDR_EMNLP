import pandas as pd

# Load the data
df = pd.read_csv('tosdr_preprocessed_data.csv')

# Find the frequency of each service
service_counts = df['Service'].value_counts()

# Find services with a frequency greater than 10
popular_services = service_counts[service_counts > 10].index

# Filter the DataFrame
filtered_df = df[df['Service'].isin(popular_services)]

# Define a dictionary for mapping labels
label_mapping = {0: "Terms of Service", 
                 1: "Privacy Policy", 
                 2: "Cookie Policy", 
                 3: "Data Policy", 
                 4: "Unknown Policy"}

# Apply the mapping to the 'Policy_type' column
filtered_df['Policy_name'] = filtered_df['Policy_type'].map(label_mapping)

# Save the filtered DataFrame to a new CSV file
filtered_df.to_csv('filtered_data_colab_1.csv', index=False)

# Now filter the DataFrame for rest of the data (services with frequency less than or equal to 10)
other_services = df[~df['Service'].isin(popular_services)]

# Apply the mapping to the 'Policy_type' column
other_services['Policy_name'] = other_services['Policy_type'].map(label_mapping)

# Save the rest of the data to another CSV file
other_services.to_csv('other_data_colab_1.csv', index=False)
