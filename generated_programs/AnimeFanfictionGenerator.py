
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = (f"Write a fanfiction story involving the anime {input('What is your favourite anime? ')} "
          f"and the video game {input('What is your favourite video game? ')}.")

completions = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
)

message = completions.choices[0].text.rstrip('\n')
print(message)
