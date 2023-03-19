# Dreamer.py

Asks you what you want the Python program to do and uses OpenAI's GPT 3.5 Turbo engine to create a Python script for it and give the user the option to automatically run it. Also installs required libraries and automatic naming (following Python standards). 

# RUN?

After generating the program, it will give you the option to automatically run it. 
The program is then stored in the /generated_programs folder and opened (appropriate to OS). 

# LIMITATIONS

You should only really say 'yes' to automatically run the program if the the generated program wouldn't need additional files (ie. images) otherwise it'll often just crash. Due to the nature of the model, it might try and use links to files that are outdated or no longer exist, so you might need to fix that. I'm working on a fix for that...

## NOTE: You must set your OpenAI API Key
In Terminal, 

    export OPENAI_API_KEY="YOUR_API_KEY"
    #run this to check if it is set
    echo $OPENAI_API_KEY


## INSTALL

Open Terminal

    cd where/you/want/it
    git clone https://github.com/jansdhillon/Dreamer.git
    cd Dreamer

You must have python3 and pip installed. It is also reccommended to use a virtual environment. Run:

    pip install openai

Finally, 

    python3 Dreamer.py



