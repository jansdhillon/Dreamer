
import openai
openai.api_key = "YOUR_API_KEY"
model_engine = "text-davinci-002"
prompt_text = "Write a paragraph about what it would be like if Jotaro Kujo joined the Straw Hat Pirates."

def generate_text(prompt):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

output_text = generate_text(prompt_text)
print(output_text)
