from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def tokenize(text):
    # Tokenization using regex to split by non-word characters
    tokens = re.findall(r'\b\w+\b', text)
    return tokens

@app.route('/tokenize', methods=['POST'])
def tokenize_string():
    # Get JSON data from the request
    data = request.get_json()
    
    # Check if 'text' is in the JSON data
    if 'text' not in data:
        return jsonify({"error": "No text provided"}), 400
    
    # Tokenize the provided text
    tokens = tokenize(data['text'])
    
    # Return the tokens as a JSON response
    return jsonify(tokens)

if __name__ == '__main__':
    app.run(debug=True)