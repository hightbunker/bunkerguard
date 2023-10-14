from flask import Flask, request, jsonify, render_template
from flask_cors import CORS  
from decouple import config  # <-- Import config from python-decouple
import openai

app = Flask(__name__)
CORS(app)  

# Use the API Key from environment variable
openai.api_key = config('OPENAI_API_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    response = openai.Completion.create(
      engine="davinci",
      prompt=user_message,
      max_tokens=150
    )

    return jsonify({"response": response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
