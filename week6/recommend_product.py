import pandas as pd

# Sample data: Users and their purchased products
data = {
    'user_id': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5],
    'product_id': [101, 102, 101, 103, 102, 104, 105, 106, 107, 108]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create a list of products
products = {
    101: 'Laptop',
    102: 'Headphones',
    103: 'Smartphone',
    104: 'Tablet',
    105: 'Mouse',
    106: 'Keyboard',
    107: 'Monitor',
    108: 'Printer'
}


# Function to recommend products
def recommend_products(user_id, df):

    # Get products purchased by the user
    purchased_products = df[df['user_id'] == user_id]['product_id'].tolist()

    # Find users who purchased the same products
    similar_users = df[df['product_id'].isin(purchased_products)]['user_id'].unique()

    # Find products purchased by these similar users
    recommended_products = df[df['user_id'].isin(similar_users)]['product_id'].unique()

    # Exclude products already purchased by the user
    recommended_products = [p for p in recommended_products if p not in purchased_products]

    # Get product names
    recommended_product_names = [products[pid] for pid in recommended_products]

    return recommended_product_names


# Example: Recommend products for user 1
user_id = 1
recommendations = recommend_products(user_id, df)
print(f"Recommended products for user {user_id}: {recommendations}")
