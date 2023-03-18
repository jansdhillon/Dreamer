# Dreamer.py

Asks you what you want the Python program to do and uses OpenAI's GPT 3.5 Turbo engine to create a Python script for it and give the user the option to automatically run it. Also installs required libraries and automatic naming (following Python Standards). 

## NOTE: You must set your OpenAI API Key

    export OPENAI_API_KEY="YOUR_API_KEY"


## INSTALL

Open Terminal

    cd where/you/want/it
    git clone https://github.com/jansdhillon/Dreamer.git
    cd Dreamer

You must have python3 and pip installed. It is also reccommended to use a virtual environment. Run

    pip install openai

Finally, 

    python3 Dreamer.py


After generating the program, it will give you the option to automatically run it. Only do this if the the generated program wouldn't need additional files (ie. images) otherwise it'll just crash. It is then stored in the /generated_programs folder and opened (appropriate to OS). 
