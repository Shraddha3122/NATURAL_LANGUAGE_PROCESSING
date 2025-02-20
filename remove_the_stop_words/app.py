from flask import Flask, request, jsonify
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

app = Flask(__name__)

# Load stop words
stop_words = set(stopwords.words('english'))

@app.route('/remove_stopwords', methods=['GET'])
def remove_stopwords():
    sentence = request.args.get('text', '')  
    words = sentence.split() 
    filtered_words = [word for word in words if word.lower() not in stop_words] 
    result = ' '.join(filtered_words) 

    return jsonify({"original": sentence, "filtered": result})

if __name__ == '__main__':
    app.run(debug=True)
