from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

# Set up your OpenAI API Key
openai.api_key = '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'

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
