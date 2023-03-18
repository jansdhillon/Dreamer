
import os

string = input("Enter a string: ")
vowels = "aeiouAEIOU"
for char in vowels:
    string = string.replace(char, "x")

print(string)
