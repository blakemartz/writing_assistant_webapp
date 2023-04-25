from flask import Flask, render_template, request, jsonify
from gpt_api import imitate_style
from welcome import WELCOME

app = Flask(__name__)

@app.route('/')
def home():
    num_text_inputs = 3
    specific_texts = [WELCOME[0], WELCOME[1], WELCOME[2]]
    return render_template('index.html', num_text_inputs=num_text_inputs, specific_texts=specific_texts)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    user_texts = data.get('text_inputs', [])
    subject_input = data.get('subject_input')

    # Call the imitate_style function with user_texts as a parameter
    generated_text = imitate_style(user_texts, subject_input)

    return jsonify(generated_text=generated_text)


if __name__ == '__main__':
    app.run(debug=True)
