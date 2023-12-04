def find_preceding_alphabet(char):
    if char.isalpha() and len(char) == 1:
        char_lower = char.lower()
        if char_lower == 'a':
            preceding_alphabet = 'z'
        else:
            preceding_alphabet = chr(ord(char_lower) - 1)
        return preceding_alphabet
    else:
        return "Invalid input. Please provide a single alphabet."

# Example usage:
input_alphabet = input("Enter an alphabet: ")
result = find_preceding_alphabet(input_alphabet)
print(f"The preceding alphabet of {input_alphabet} is {result}.")
