from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Create the sentiment analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()

# Input text for sentiment analysis
transcribed_text = input("ENTER THE TEXT YOU WANT TO ANALYZE: ")

# Perform sentiment analysis on the input text
sentiment_scores = sentiment_analyzer.polarity_scores(transcribed_text)

# Calculate a sentiment score out of 10 based on the compound score
# Map the compound score to a range of 0 to 10
sentiment_score_out_of_10 = ((sentiment_scores['compound'] + 1) / 2) * 10

# Display the sentiment analysis result
print(f"Transcribed Text: {transcribed_text}")
print(f"Sentiment Score (out of 10): {sentiment_score_out_of_10:.2f}")























