import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


# Function to pre-process a review
def pre_process_review(review):
    # Tokenize the review
    tokens = word_tokenize(review)

    # Convert to lower case
    tokens = [word.lower() for word in tokens]

    # Remove punctuation and non-alphabetic tokens
    tokens = [word for word in tokens if word.isalpha()]

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens


# Function to calculate BoW matrix
def calculate_bow_matrix(reviews):
    # Join token lists into strings
    reviews_str = reviews.apply(lambda x: ' '.join(x))

    # Initialize CountVectorizer
    vectorizer = CountVectorizer()

    # Fit and transform the data to create the BoW matrix
    bow_matrix = vectorizer.fit_transform(reviews_str)

    # Convert to DataFrame for easy viewing
    bow_df = pd.DataFrame(bow_matrix.toarray(), columns=vectorizer.get_feature_names_out())

    return vectorizer, bow_df


# Load the sentiment data file
df = pd.read_csv('review_data.csv')

# Pre-process the reviews
df['processed_review'] = df['review'].apply(pre_process_review)

# Display pre-processed reviews
print("Pre-Processed Reviews:")
print(df['processed_review'])

# Calculate the full BoW matrix
vectorizer, bow_df = calculate_bow_matrix(df['processed_review'])

# Display the full BoW matrix
print("\nBoW Matrix:")
print(bow_df)

# Split the BoW matrix based on sentiment
positive_bow_df = bow_df[df['sentiment'] == 'positive']
negative_bow_df = bow_df[df['sentiment'] == 'negative']

# Display the positive and negative BoW matrices
print("\nPositive BoW Matrix:")
print(positive_bow_df)

print("\nNegative BoW Matrix:")
print(negative_bow_df)


# Function to predict sentiment using cosine similarity
def predict_sentiment(new_reviews, vectorizer, positive_bow_df, negative_bow_df):
    # Pre-process new reviews
    new_reviews_processed = new_reviews.apply(pre_process_review)

    # Join token lists into strings
    new_reviews_str = new_reviews_processed.apply(lambda x: ' '.join(x))

    # Transform the new reviews to BoW representation
    new_reviews_bow = vectorizer.transform(new_reviews_str)

    predictions = []

    for i in range(new_reviews_bow.shape[0]):
        new_review_vector = new_reviews_bow[i]

        # Calculate cosine similarity
        positive_similarity = cosine_similarity(new_review_vector, positive_bow_df).mean()
        negative_similarity = cosine_similarity(new_review_vector, negative_bow_df).mean()

        # Predict sentiment based on highest similarity
        if positive_similarity > negative_similarity:
            predictions.append("positive")
        elif positive_similarity < negative_similarity:
            predictions.append("negative")
        else:
            predictions.append("neutral")

    return predictions


# Load new reviews for prediction
test_reviews = pd.read_csv('review_data.csv')

# Predict sentiment of new reviews
predictions = predict_sentiment(test_reviews['review'], vectorizer, positive_bow_df, negative_bow_df)

# Display predictions
print("\nPredicted Sentiments:")
for review, sentiment in zip(test_reviews['review'], predictions):
    print(f"Review: {review}\nPredicted Sentiment: {sentiment}\n")
