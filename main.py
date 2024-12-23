def main(): 
    PATH_TO_BOOK = "books/frankenstein.txt"

    text = get_text(PATH_TO_BOOK)
    print(f"This is the text inside {PATH_TO_BOOK[6:]}: \n{text}")
    word_count = count_words(text)
    print(f"The word count in the {PATH_TO_BOOK[6:]} is {word_count} words")
    char_count = count_chars(text)
    print(f"The character count in the {PATH_TO_BOOK[6:]} is the following: \n{char_count}")

def get_text(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text: str) -> int:
    word_list = text.split()
    word_count = len(word_list)
    return word_count

def count_chars(text: str) -> dict[str: int]:
    characters_dict = {}
    for char in text:
        char_lower = char.lower()
        if char_lower in characters_dict:
            characters_dict[char_lower] += 1
        else: 
            characters_dict[char_lower] = 1
    return characters_dict

main()