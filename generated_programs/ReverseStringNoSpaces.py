
input_string = input("Enter a string: ")
input_string = input_string.replace(" ", "")
sorted_string = sorted(input_string, reverse=True)
sorted_string = "".join(sorted_string)
print(sorted_string)
