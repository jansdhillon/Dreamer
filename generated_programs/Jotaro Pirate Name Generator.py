
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = "Jotaro Kujo joins the Straw Hat Pirates"

model_engine = "text-davinci-003"

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.7,
)

message = completions.choices[0].text
print(message)
