def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Example
print(are_anagrams("listen", "silent"))  # Output: True
print(are_anagrams("hello", "world"))    # Output: False
