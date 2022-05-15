from flask import Flask, render_template, request
from textblob import TextBlob
from langdetect import detect
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)
lang_map = {'Tamil': 'ta', 'English': 'en', 'French': 'fr', 'Bengali': 'bn'}

@app.route("/")
def home():
    return render_template('home.html', output=None)

@app.route("/predict", methods=['POST'])
def predict():
    words = str(request.form.get('from_language'))
    final_words = TextBlob(words)
    final_language = detect(words)
    to_language = str(request.form.get('lang'))
    translate_word = final_words.translate(from_lang=final_language, to= lang_map[to_language])
    return render_template('home.html', output=translate_word,)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

