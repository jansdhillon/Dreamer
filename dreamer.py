import os
import openai
import requests
import stat
import textwrap
from pathlib import Path
import re

def main():
    # Set up the OpenAI API client
    openai.api_key = os.getenv("OPENAI_API_KEY")

    # Ask the user for the program's purpose
    prompt = input("What should the program do? ")


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [
        {"role": "system", "content": "You are an AI language model that generates Python code."},
        {"role": "user", "content": f"Create a Python script to {prompt}. Only generate the code needed for the program to run"},
        {"role": "user", "content": f"modify that to make the the code block work. Return ONLY the python code and don't explain it. Remove any text that is not part of the code itself"}]
    )

    code = response.choices[0].message.content
    
    code = extract_code_from_markdown(code)

    name = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [{"role": "user", "content": f"Come up with a name to accurately represent this program: {code}. Return ONLY the name and don't explain it. Remove any text that is not part of the name itself"}]
    )

    name = name.choices[0].message.content.strip()
    print(name)


    # Create the Python file and write the generated code to it
    filename = name + ".py"
    with open(filename, "w") as f:
        f.write(code)

    # Download and save any required libraries
    required_libraries = extract_required_libraries(code)
    if required_libraries:
        download_and_save_libraries(required_libraries)

    print(f"\nGenerated program '{filename}' successfully created.")

    run = input("Run the program? y/n ")
    
    if run.lower() == "y":
        os.system(f"python {filename}")


    



def extract_required_libraries(code):
    import_statements = [line.strip() for line in code.splitlines() if line.startswith("import") or line.startswith("from")]
    libraries = [statement.split()[1] for statement in import_statements if "import" in statement]
    return libraries


def download_and_save_libraries(libraries):
    for lib in libraries:
        try:
            print(f"Installing '{lib}'...")
            os.system(f"pip install {lib}")
        except Exception as e:
            print(f"Failed to install '{lib}': {e}")

def extract_code_from_markdown(text):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo",
#         messages = [
#         {"role": "system", "content": "You are an AI language model that generates Python code."},
        
#         temperature=1,
#     )
    #remove markdown syntax from the response
    text = re.sub(r'```python', '', text)
    text = re.sub(r'```', '', text)

    return text




if __name__ == "__main__":
    main()