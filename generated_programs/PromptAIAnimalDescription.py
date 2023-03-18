
import openai_secret_manager
import openai
import os

openai.api_key = openai_secret_manager.get_secret("openai")["api_key"]
animal = input("Enter your favourite animal: ")
prompt = "Write a brief description of " + animal
completions = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=60,
    n=1,
    stop=None,
    temperature=0.5,
)
message = completions.choices[0].text.strip()
print(message)
