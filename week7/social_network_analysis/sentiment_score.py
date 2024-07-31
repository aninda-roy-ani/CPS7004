# Define lists of positive and negative words
positive_words = ['happy', 'good', 'great', 'fantastic', 'wonderful', 'love', 'excellent', 'amazing']
negative_words = ['sad', 'bad', 'terrible', 'awful', 'worst', 'hate', 'poor', 'horrible']


def analyze_sentiment(text):
    
    # Tokenize the text into words
    words = text.lower().split(' ')

    # Initialise sentiment scores
    positive = 0
    negative = 0

    # Calculate the sentiment score
    for word in words:
        if word in negative_words:
            negative = negative + 1
        elif word in positive_words:
            positive = positive + 1

    # Determine overall sentiment (neutral by default)
    sentiment = 'Neutral'
    if negative > positive:
        sentiment = 'Negative'
    elif positive > negative:
        sentiment = 'Positive'
    return sentiment


# Example usage
text = "I love the wonderful and fantastic weather, but I hate the bad traffic."
result = analyze_sentiment(text)
print(f"The sentiment of the text is: {result}")