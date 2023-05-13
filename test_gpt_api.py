from unittest.mock import MagicMock, patch
from gpt_api import imitate_style, generate_text


def test_generate_text():
    chat_thread = [
        {"role": "system", "content": "You are an AI."},
        {"role": "user", "content": "Generate some text for me."},
    ]

    with patch("openai.ChatCompletion.create") as mock_chat_completion_create:
        mock_chat_completion_create.return_value = MagicMock(choices=[
            MagicMock(message={"content": "This is the generated text."})
        ])

        generated_text = generate_text(chat_thread, "fake_api_key", "gpt-3.5-turbo")

    assert generated_text == "This is the generated text."



def test_imitate_style():
    user_texts = [
        "This is the first example text.",
        "This is the second example text.",
        "This is the third example text.",
    ]

    subject_input = "testing subject"

    model_selection = "gpt-4"

    with patch("gpt_api.generate_text") as mock_generate_text:
        mock_generate_text.return_value = "This is the generated text imitating the style of the examples."

        generated_text = imitate_style(user_texts, subject_input, model_selection)

    assert generated_text == "This is the generated text imitating the style of the examples."



## Tests actual API calls ##
# def test_api_without_subject():
#     test_text = "Test"
#     generated_text = imitate_style(user_texts=test_text)
#     print(f"Test without subject: {generated_text}")
#     assert generated_text != None

# def test_api_with_subject():
#     test_text = "Test"
#     test_subject = "This is a test"
#     generated_text = imitate_style(user_texts=test_text, subject_input=test_subject)
#     print(f"Test with subject: {generated_text}")
#     assert generated_text != None