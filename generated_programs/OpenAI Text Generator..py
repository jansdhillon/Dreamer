import openai
import os

openai.api_key = os.environ["OPENAI_API_KEY"] #Insert your API key here

def generate_text(prompt):
    response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            temperature=0.5,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

    message = response.choices[0].text
    return message

prompt = "Jotaro Kujo joins the Straw Hat Pirates."
message = generate_text(prompt)
print(message)