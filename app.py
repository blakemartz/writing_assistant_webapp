from flask import Flask, render_template, request
from gpt_api import imitate_style

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    user_texts = []
    for i in range(1, 4):  # Adjust the range based on the number of textarea inputs
        user_sample = request.form.get(f'text_input{i}')
        if user_sample:
            user_texts.append(f"The following is a writing example: '{user_sample}'")

    # Call the imitate_style function with user_texts as a parameter
    generated_text = imitate_style(user_texts)

    return generated_text


if __name__ == '__main__':
    app.run(debug=True)
