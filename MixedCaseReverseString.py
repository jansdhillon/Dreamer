
user_input = input("Enter a string: ")

new_str = user_input.replace(" ", "")

sorted_str = sorted(new_str, reverse=True)

final_str = ""

for char in sorted_str:
    if char.islower():
        final_str += char.upper()
    else:
        final_str += char.lower()

print(final_str)



user_input = input("Enter a string: ")
new_str = user_input.replace(" ", "")
sorted_str = sorted(new_str, reverse=True)
final_str = ""
for char in sorted_str:
    if char.islower():
        final_str += char.upper()
    else:
        final_str += char.lower()
print(final_str)
