import os

# Directory to save the text files
output_dir = 'output_texts'
os.makedirs(output_dir, exist_ok=True)

# Alphabet excluding 'k' and 'w'
alphabet = "abcdefghijlmnopqrstuvxyz"

# Generate text files
for letter in alphabet:
    file_path = os.path.join(output_dir, f"{letter}.txt")
    with open(file_path, 'w') as file:
        file.write(f"{letter}")

print("Text files generated successfully.")