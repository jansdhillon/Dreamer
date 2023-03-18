
import os

dir_path = os.getcwd()

for file in os.listdir(dir_path):
    if file.startswith("file") and file.endswith(".txt"):
        os.remove(os.path.join(dir_path, file))
