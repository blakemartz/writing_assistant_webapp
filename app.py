from flask import Flask, render_template, request, jsonify
from gpt_api import imitate_style
from welcome import WELCOME

app = Flask(__name__)

PLACEHOLDER = WELCOME

@app.route('/')
def home():
    num_text_inputs = 3
    specific_texts = [PLACEHOLDER[0], PLACEHOLDER[1], PLACEHOLDER[2]]
    return render_template('index.html', num_text_inputs=num_text_inputs, specific_texts=specific_texts)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    user_texts = data.get('text_inputs', [])

    # Call the imitate_style function with user_texts as a parameter
    generated_text = imitate_style(user_texts)

    return jsonify(generated_text=generated_text)


if __name__ == '__main__':
    app.run(debug=True)
