#Write a Program to find the parts of speech of the words in a sentence.
#sentence = "The Dog killed the rats."

from flask import Flask, request, jsonify
import nltk

# Initialize the Flask application
app = Flask(__name__)

# Ensure NLTK resources are downloaded
nltk.download('punkt', quiet=True)
nltk.download('averaged_perceptron_tagger', quiet=True)

@app.route('/pos', methods=['POST'])
def pos_tagging():
    # Get the sentence from the request
    data = request.get_json()
    sentence = data.get('sentence', '')

    # Tokenize the sentence
    words = nltk.word_tokenize(sentence)

    # Get the parts of speech
    pos_tags = nltk.pos_tag(words)

    # Return the result as JSON
    return jsonify(pos_tags)

if __name__ == '__main__':
    app.run(debug=True)