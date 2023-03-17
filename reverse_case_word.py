```python
def reverse_string(string):
    reversed_string = ""
    for char in string:
        if char == " ":
            reversed_string += char
        elif char.isupper():
            reversed_string += char.lower()
        else:
            reversed_string += char.upper()
    return reversed_string[::-1]

user_input = input("Enter a string: ")
print(reverse_string(user_input))
```