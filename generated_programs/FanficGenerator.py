
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_fanfic(prompt_movie, prompt_game):
    prompt = f"{prompt_movie} meets {prompt_game} in a fanfic"
    model = "text-davinci-003"
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

movie = input("What is your favourite movie? ")
game = input("What is your favourite video game? ")

print(generate_fanfic(movie, game))
