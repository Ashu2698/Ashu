def count_words_chars_lines(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        word_count = len(text.split())
        char_count = len(text)
        line_count = text.count('\n') + 1  # Add 1 for the last line if it doesn't end with a newline
    return word_count, char_count, line_count

def main():
    file_path = input("Enter the path to the text document: ")
    try:
        word_count, char_count, line_count = count_words_chars_lines(file_path)
        print(f"Number of words: {word_count}")
        print(f"Number of characters: {char_count}")
        print(f"Number of lines: {line_count}")
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")

if __name__ == "__main__":
    main()
