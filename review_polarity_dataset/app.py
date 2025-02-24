# Do sentiment analysis using NLP and classify the movie reviews into good or bad.




import nltk

# Download the VADER lexicon
nltk.download('vader_lexicon')

from flask import Flask, request, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = Flask(__name__)
sia = SentimentIntensityAnalyzer()

def analyze_sentiment(review):
    score = sia.polarity_scores(review)
    return "Good" if score['compound'] >= 0.05 else "Bad"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    review = data.get('review', '')
    sentiment = analyze_sentiment(review)
    return jsonify({'sentiment': sentiment})

if __name__ == '__main__':
    app.run(debug=True)