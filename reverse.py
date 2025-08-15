# Reverse a string using slicing
string = "Hello, World!"
reversed_string = string[::-1]
print("Reversed String:", reversed_string)


# Reverse a string using the reversed() function
string = "Hello, World!"
reversed_string = ''.join(reversed(string))
print("Reversed String:", reversed_string)



# Reverse a string using a loop
string = "Hello, World!"
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print("Reversed String:", reversed_string)
