from flask import Flask, jsonify
import re

app = Flask(__name__)

# The string to be tokenized
text = "Twinkle twinkle little star, now I wonder what you are, up above the world so high. Like a diamond in the sky."

def tokenize(text):
    # Tokenization using regex to split by non-word characters
    tokens = re.findall(r'\b\w+\b', text)
    return tokens

@app.route('/tokenize', methods=['GET'])
def tokenize_string():
    tokens = tokenize(text)
    return jsonify(tokens)

if __name__ == '__main__':
    app.run(debug=True)