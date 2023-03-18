import os
import openai
import re
import sys
import tkinter as tk
import platform
import subprocess

openai.api_key = os.getenv("OPENAI_API_KEY")

def write_program(prompt):
    def extract_required_libraries(code):
        import_statements = [line.strip() for line in code.splitlines(
        ) if line.startswith("import") or line.startswith("from")]
        libraries = [statement.split()[1]
                    for statement in import_statements if "import" in statement]
        return libraries


    def download_and_save_libraries(libraries):
        for lib in libraries:
            try:
                print(f"Installing '{lib}'...")
                os.system(f"pip install {lib}")
            except Exception as e:
                print(f"Failed to install '{lib}': {e}")


    def extract_code_from_markdown(text):
        text = re.sub(r'```python', '', text)
        text = re.sub(r'```', '', text)
        return text


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI language model that generates Python code."},
            {"role": "user", "content": f"Create a Python script to {prompt}. Only generate the code needed for the program to run. Return ONLY the python code and don't explain it. Ensure your response is valid Python code. Remove any text that is not part of the code itself and do not put it in quotes. Assume API keys are already stored as environment variables and access them using getenv."},]
    )

    raw_code = response.choices[0].message.content

    code = extract_code_from_markdown(raw_code)

    response2 = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"Come up with a name to accurately represent this program: {code}. Return ONLY the name and don't explain it. Do not put it in quotes. Separate words with spaces following Python standards."}]
    )

    raw_name = response2.choices[0].message.content
    name = "".join(raw_name.split())

    print(name)

    # Create the Python file and write the generated code to it
    filename = name + ".py"
    with open(f"generated_programs/{filename}", "w") as f:
        f.write(code)

    # Download and save any required libraries
    required_libraries = extract_required_libraries(code)
    if required_libraries:
        download_and_save_libraries(required_libraries)

    print(f"\nGenerated program '{filename}' successfully created.")

    return filename

def get_input():
    # start gui
    root = tk.Tk()
    root.title("Dreamer")

    # create entry
    label = tk.Label(root, text="What should the program do?")
    label.pack()
    entry = tk.Text(root)
    entry.pack()

    def get_answer():
        answer = entry.get("1.0", tk.END)
        program = write_program(answer)
        # Create frame in the center of the screen
        ask_to_run_frame = tk.Frame(root)
        ask_to_run = tk.Label(ask_to_run_frame, text="Would you like to run the program?")

        ask_to_run.pack()
        ask_to_run_frame.pack(expand=True, anchor=tk.CENTER)  # Center the frame

        def yes():
            os.system(f"python3 generated_programs/{program}")
            # Open file
            open_file(f"generated_programs/{program}")
            root.destroy()

        yes_button = tk.Button(ask_to_run_frame, text="Yes", command=yes)
        yes_button.pack(side=tk.LEFT)
        no_button = tk.Button(ask_to_run_frame, text="No", command=root.destroy)
        no_button.pack(side=tk.LEFT)

        def open_file(file_path):
            system = platform.system()

            if system == "Windows":
                os.startfile(file_path)
            elif system == "Darwin":
                subprocess.Popen(["open", file_path])
        

    # create button
    button = tk.Button(root, text="Submit", command=get_answer)
    button.pack()

    # run gui
    root.mainloop()


def main():

    try:
        # Create a folder to store the generated programs
        path = os.path.dirname(os.path.realpath(sys.argv[0]))
        os.makedirs(path+"/generated_programs", exist_ok=True)
        path = path+"/generated_programs"

        # Ask the user for the program's purpose
        get_input()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
