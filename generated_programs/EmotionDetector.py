
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def detect_emotion(prompt: str):
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.choices[0].text.strip()

user_input = input("Say something: ")
emotion = detect_emotion(user_input)
print("Detected emotion:", emotion)
