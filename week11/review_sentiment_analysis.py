import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')


def pre_process_review(text):

    tokens = word_tokenize(text)
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]
    lemmatized_tokens = [lemmatizer.lemmatize(word) for word in filtered_tokens]
    return lemmatized_tokens

def calculate_bow_matrix(vectorizer, reviews, sentiments):
    reviews_str = reviews.apply(lambda x: ' '.join(x))
    bow_matrix = vectorizer.fit_transform(reviews_str)

    positive_bow = bow_matrix[sentiments == 'positive']
    negative_bow = bow_matrix[sentiments == 'negative']

    positive_bow_df = pd.DataFrame(positive_bow.toarray(), columns=vectorizer.get_feature_names_out())
    negative_bow_df = pd.DataFrame(negative_bow.toarray(), columns=vectorizer.get_feature_names_out())

    return positive_bow_df, negative_bow_df


if __name__ == '__main__':

    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    vectorizer = CountVectorizer()

    data = pd.read_csv('review_data.csv')

    # Assuming the statements are in a column named 'review'
    # Apply the pre_process_review function to each review
    # data['review'] = data['review'].apply(pre_process_review)
    data['processed_review'] = data['review'].apply(lambda x:pre_process_review(x))

    positive_bow_df, negative_bow_df = calculate_bow_matrix(vectorizer, data['processed_review'], data['sentiment'])

    # Display the first few rows of the DataFrame
    print(data['processed_review'].head(10))

    print(positive_bow_df.to_numpy())

    print(negative_bow_df.to_numpy())


