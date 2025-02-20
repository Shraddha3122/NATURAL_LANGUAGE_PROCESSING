from flask import Flask, jsonify
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk

# Download required resources
nltk.download('wordnet')
nltk.download('omw-1.4')

app = Flask(__name__)
lemmatizer = WordNetLemmatizer()

@app.route('/lemmatize', methods=['GET'])
def lemmatize_words():
    words = ['give', 'giving', 'given', 'gave']
    lemmatized_words = {word: lemmatizer.lemmatize(word, wordnet.VERB) for word in words}
    return jsonify(lemmatized_words)

if __name__ == '__main__':
    app.run(debug=True)