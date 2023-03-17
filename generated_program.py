
import string

filename = "alphabet.txt"

with open(filename, "w") as f:
    f.write(string.ascii_lowercase)
