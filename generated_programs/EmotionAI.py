
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def classify_emotion(sentence):
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Classify the emotion in the following sentence: '{sentence}'",
        temperature=0.5,
        max_tokens=1,
        n=1,
        stop=None,
        )
    return response.choices[0].text.strip()
