import pandas as pd

# Load the data

df = pd.read_csv('transactions.csv')

# Calculate mean and standard deviation
mean_amount = df['amount'].mean()
std_amount = df['amount'].std()

# Compute Z-scores
df['z_score'] = (df['amount'] - mean_amount) / std_amount

# Flag anomalies (Z-score > 3 or Z-score < -3)
threshold = 1.5
df['is_anomaly'] = df['z_score'].abs() > threshold

print(df.head(20))