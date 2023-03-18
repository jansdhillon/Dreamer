
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def detect_sentiment(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Sentiment analysis of the text: {text} is",
        temperature=0,
        max_tokens=1,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    sentiment = response.choices[0].text
    if "Positive" in sentiment:
        return "Positive"
    elif "Negative" in sentiment:
        return "Negative"
    else:
        return "Neutral"

user_text = input("Enter your text: ")

print(detect_sentiment(user_text))
