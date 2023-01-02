# Read the string from the standard input
s = input()

# Initialize variables to keep track of the current character and its count
current_char = s[0]
char_count = 1

# Iterate through the characters in the string
for i in range(1, len(s)):
    # If the current character is the same as the previous character, increment the count
    if s[i] == current_char:
        char_count += 1
    # If the current character is different from the previous character, output the previous character and its count
    else:
        print(current_char + str(char_count), end="")
        current_char = s[i]
        char_count = 1

# Output the last character and its count
print(current_char + str(char_count))
