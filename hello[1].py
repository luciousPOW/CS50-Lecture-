
# Ask user for their name
name = input("What's your name? ")
# Split user's name into first name and last name
first, last = name.split(" ")

# Remove whitespace from str
name = name.strip()

# Capitalization
name = name.capitalize()

# Display user input using fstring (format string)
print(f"Hello, {name}")
