import pandas as pd

# Load transaction data
data = pd.read_csv('transactions.csv')

# Rule 1: High Amount Transactions
data['rule_1'] = data['amount'] > 3000


# Rule 2: Unusual Transaction Times
def is_night_time(transaction_time):
    hour = transaction_time.hour
    return 0 <= hour < 6


data['transaction_time'] = pd.to_datetime(data['transaction_time'])
data['rule_2'] = data['transaction_time'].apply(is_night_time)

# Rule 3: Rapid Succession Transactions
data['transaction_hour'] = data['transaction_time'].dt.hour
data['transaction_date'] = data['transaction_time'].dt.date

data['rule_3'] = data.groupby(['customer_id', 'transaction_date', 'transaction_hour'])['transaction_id'].transform('count') > 3

# Rule 4: Frequent High-Value Transactions
data['rule_4'] = data.groupby(['customer_id', 'transaction_date'])['amount'].transform(lambda x: (x > 2000).sum()) > 5

# Rule 5: High-Risk Transaction Types
data['rule_5'] = (data['transaction_type'] == 'withdrawal') & (data['amount'] > 1000)

# Rule 6: Multiple Merchant Transactions
data['rule_6'] = data.groupby(['customer_id', 'transaction_date'])['merchant_id'].transform('nunique') > 3

# Combine rules: If any rule is true, flag the transaction as suspicious
data['is_suspicious'] = data[['rule_1', 'rule_2', 'rule_3', 'rule_4', 'rule_5', 'rule_6']].any(axis=1)

# Print the result
print(data[['transaction_id', 'amount', 'transaction_time', 'is_suspicious']])