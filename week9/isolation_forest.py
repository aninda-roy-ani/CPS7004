import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import OneHotEncoder

# Load the data
df = pd.read_csv('transactions.csv')

# One-hot encode the transaction_type column
encoder = OneHotEncoder(sparse_output=False)
transaction_type_encoded = encoder.fit_transform(df[['transaction_type']])
transaction_type_encoded_df = pd.DataFrame(transaction_type_encoded, columns=encoder.get_feature_names_out(['transaction_type']))

# Concatenate the encoded transaction_type with the original dataframe
df = pd.concat([df, transaction_type_encoded_df], axis=1)

# Fit the Isolation Forest model
features = ['amount'] + list(transaction_type_encoded_df.columns)
model = IsolationForest(contamination=0.1, random_state=42)
df['is_anomaly_iforest'] = model.fit_predict(df[features])

# Mapping the output of Isolation Forest to more understandable labels
df['is_anomaly_iforest'] = df['is_anomaly_iforest'].map({1: False, -1: True})

# Display the results
print(df[['transaction_id', 'amount', 'transaction_type', 'is_anomaly_iforest']])


