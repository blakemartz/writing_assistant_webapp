from dotenv import load_dotenv

load_dotenv()

import os
import openai

MODEL = "gpt-3.5-turbo"
MAX_TOKENS = 1000
TEMPERATURE = 0.8


def generate_text(chat_thread, api_key):
    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=chat_thread,
        max_tokens=MAX_TOKENS,
        n=1,
        temperature=TEMPERATURE,
    )

    if response.choices:
        generated_text = response.choices[0].message['content']
        return generated_text.strip()
    else:
        return None


# Initialize the chat thread
def imitate_style(user_texts):
    chat_thread = [
        {
            "role": "system",
            "content": "You are a creative and talented imitation agent that can analyze example texts "
                       "and generate a completely new text as if it is the user's own writing. "
                       "-Take great care to learn from the provided examples "
                       "and capture the grammar usage, phrasing style, and creative style. "
                       "-You need to match the capitalization choices and grammar style of the examples. "
                       "-Pay close attention to the spirit, vibe, and sentiment of the submitted works. "
                       "-May sure your subject matter fits in well with the provided examples. "
                       "-Do not reuse any specific phrases from the examples. "
                       "-Do not respond with anything but the imitation itself. "
                       "-Only respond with one new work of writing. "
                       "-Please match the length of the provided examples and be concise if necessary. "
        }
    ]

    # Add user texts to the chat thread
    for sample in user_texts:
        chat_thread.append({"role": "user", "content": sample})

    # Generate new writing call to the model - add to chat thread
    chat_thread.append({"role": "user", "content": "Generate a creative new text that imitates and matches the style "
                                                   "of the provided examples as instructed. "
                                                   "Be as concise as the examples."
                        })

    # Call the helper function to generate new text
    generated_text = generate_text(chat_thread=chat_thread, api_key=os.environ["OPENAI_API_KEY"])

    return generated_text

# # output generated text
# if generated_text:
#     print(f"{generated_text}")
#
# # Update the chat thread with the generated text
# chat_thread.append({"role": "assistant", "content": generated_text})
