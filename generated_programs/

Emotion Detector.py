
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def detect_emotion(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response.choices[0].text

prompt = input("Say something: ")
emotion = detect_emotion(prompt)
print(f"Detected emotion: {emotion}")
