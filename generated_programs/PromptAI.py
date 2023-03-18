
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = input("Say something: ")

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=prompt,
  max_tokens=1,
  n=1,
  stop=None,
  temperature=0.7,
)

print(response["choices"][0]["text"].strip())
