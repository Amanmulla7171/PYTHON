def longest_unique_substring(string):
    substring = ""
    max_length = 0
    result = ""

    for char in string:
        if char in substring:
            # Remove characters up to the repeated one
            substring = substring[substring.index(char) + 1:]
        substring += char
        if len(substring) > max_length:
            max_length = len(substring)
            result = substring

    return result

# Test cases
print(longest_unique_substring("character"))  # Output: "racte"
print(longest_unique_substring("standfan"))   # Output: "standf"
