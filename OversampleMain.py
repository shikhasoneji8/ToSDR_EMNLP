# Import necessary libraries
import pandas as pd
import numpy as np
from Oversampler import Oversampler

# Load and preprocess the training data
train_df = pd.read_csv('filtered_data_colab_clean.csv')

# Ensure that the text data is string
train_df['Description'] = train_df['Description'].astype(str)

train_texts = train_df['Description']
train_cases = train_df['Case']

# train_texts = np.array(train_texts)
# train_cases = np.array(train_cases)


sampler = Oversampler()

features, labels = sampler.oversample(train_texts, train_cases)
features = features.tolist()
features = [''.join(ele) for ele in features]

outputDf = pd.DataFrame({'Description': features, 'Case': labels})
outputDf.to_csv('pickledOversampleCaseMulticlass_filtered_data_colab_clean.csv', index=False)
#outputDf.to_pickle('pickledOversampleCaseMulticlass_test_data_clean.pkl')

