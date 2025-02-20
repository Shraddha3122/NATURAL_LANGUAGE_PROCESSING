from flask import Flask, jsonify
from nltk.stem import PorterStemmer
import nltk

# Download the NLTK data files (only need to do this once)
nltk.download('punkt')

app = Flask(__name__)

@app.route('/stem', methods=['GET'])
def stem_words():
    words = ['give', 'giving', 'given', 'gave']
    stemmer = PorterStemmer()
    stemmed_words = [stemmer.stem(word) for word in words]
    
    return jsonify({
        'original_words': words,
        'stemmed_words': stemmed_words
    })

if __name__ == '__main__':
    app.run(debug=True)