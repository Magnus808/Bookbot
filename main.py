import logging

# Set up logging
logging.basicConfig(level=logging.ERROR)

def read_file():
    while True:
        path_to_file = input("Enter the path to the file, or type 'quit' to quit: ")

        if path_to_file.lower() == 'quit':
            print("Exiting the program.")
            exit()  # Exit the program

        try:
            with open(path_to_file, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f"Error: The file {path_to_file} does not exist.")
        except IOError:
            print(f"Error: Could not read the file {path_to_file}.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def main():
    # Main execution
    file_contents = read_file()
    print("File read successfully.")
    print(f"File size: {len(file_contents)} bytes")

    # Call the word_count function
    word_count(file_contents)

def word_count(file_contents):
    # Split the file contents into words
    words = file_contents.split()
    print(f"Word count: {len(words)}")
    
if __name__ == "__main__":
    main()

def letters():
    path_to_file = "text.txt"
    letter_counts = {}  # Initialize a dictionary to hold letter counts
    with open(path_to_file) as f:
        text = f.read().lower()  # Convert text to lowercase to avoid duplicates
    for x in text:
        if x.isalpha():
            # Increment count for the letter x
            if x in letter_counts:
                letter_counts[x] += 1
            else:
                letter_counts[x] = 1
    return letter_counts  # Return the dictionary with letter counts

letter_counts = {}

# Open the file and traverse each character
with open("books/frankenstein.txt", "r") as file:
    for line in file:
        for char in line:
            # Convert to lowercase and check if it's a letter
            char = char.lower()
            if char.isalpha():
                if char in letter_counts:
                    letter_counts[char] += 1
                else:
                    letter_counts[char] = 1

# Display the results
for letter, count in letter_counts.items():
    print(f"The '{letter}' character was found {count} times")
