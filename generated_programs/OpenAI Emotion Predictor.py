
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = input("Enter some text: ")
model_engine = "text-davinci-002"
response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=0.5,
    max_tokens=1,
    n=1,
    stop=None,
)
emotion = response.choices[0].text.strip()
print(emotion)
