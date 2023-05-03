from gpt_api import imitate_style

def test_generate_without_subject():
    test_text = "Test"
    generated_text = imitate_style(user_texts=test_text)
    print(f"Test without subject: {generated_text}")
    assert generated_text

def test_generate_with_subject():
    test_text = "Test"
    test_subject = "This is a test"
    generated_text = imitate_style(user_texts=test_text, subject_input=test_subject)
    print(f"Test with subject: {generated_text}")
    assert generated_text