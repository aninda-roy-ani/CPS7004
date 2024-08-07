import pandas as pd
from sklearn.ensemble import IsolationForest

# Load the data

df = pd.read_csv('transactions.csv')


# Calculate mean and standard deviation
mean_amount = df['amount'].mean()
std_amount = df['amount'].std()

# Compute Z-scores
df['z_score'] = (df['amount'] - mean_amount) / std_amount

# Flag anomalies (Z-score > 3 or Z-score < -3)
threshold = 3
df['is_anomaly_z_score'] = df['z_score'].abs() > threshold

# Fit the Isolation Forest model
model = IsolationForest(contamination=0.1, random_state=42)
df['is_anomaly_iforest'] = model.fit_predict(df[['amount']])

# Mapping the output of Isolation Forest to more understandable labels
df['is_anomaly_iforest'] = df['is_anomaly_iforest'].map({1: False, -1: True})

# Display the results
print(df.head())