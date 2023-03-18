
import openai
openai.api_key = "API_KEY"

prompt = "Write a 500 word fanfic about Jotaro Kujo joining the Straw Hat Pirates."

model_engine = "text-davinci-003"

response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=500
)

print(response.choices[0].text)
