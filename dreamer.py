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
        {"role": "user", "content": f"Create a Python script to {prompt}. Only generate the code needed for the program to run"}],
        temperature=1,
    )

    # Extract the generated Python code
    code = response.choices[0].message.content
    
    code = extract_code_from_markdown(code)


    # Create the Python file and write the generated code to it
    filename = "generated_program.py"
    with open(filename, "w") as f:
        f.write(code)

    # Make the file executable
    st = os.stat(filename)
    os.chmod(filename, st.st_mode | stat.S_IEXEC)

    # Download and save any required libraries
    required_libraries = extract_required_libraries(code)
    if required_libraries:
        download_and_save_libraries(required_libraries)

    print(f"\nGenerated program '{filename}' successfully created and made executable.")

    run = input("Run the program? y/n ")

    if run == "y":
        os.system(f"./{filename}")


    



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
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages = [
        {"role": "system", "content": "You are an AI language model that generates Python code."},
        {"role": "user", "content": f"modify {text} to make the the code block work. Return ONLY the python code and don't explain it"}],
        temperature=1,
    )
    #remove markdown syntax from the response
    text = response.choices[0].message.content
    text = re.sub(r'```python', '', text)
    text = re.sub(r'```', '', text)

    return text




if __name__ == "__main__":
    main()