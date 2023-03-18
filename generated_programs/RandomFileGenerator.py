
import random
import os

for i in range(1, 11):
    filename = f"file{i}.txt"
    with open(filename, "w") as file:
        file.write(str(random.randint(1, 100)))
