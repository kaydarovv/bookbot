def main(): 
    PATH_TO_BOOK = "books/frankenstein.txt"

    text = get_text(PATH_TO_BOOK)
    word_count = count_words(text)
    char_count = count_chars(text)
    sorted_char_count = sort_char_count(char_count)
    text_report = generate_text_report(PATH_TO_BOOK, word_count, sorted_char_count)
    print(text_report)

def get_text(path: str) -> str:
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text: str) -> int:
    word_list = text.split()
    word_count = len(word_list)
    return word_count

def count_chars(text: str) -> dict[str: int]:
    char_dict = {}
    for char in text:
        char_lower = char.lower()
        if not char_lower.isalpha():
            continue
        if char_lower in char_dict:
            char_dict[char_lower] += 1
        else: 
            char_dict[char_lower] = 1
    return char_dict

def sort_char_count(char_dict: dict) -> dict:
    def sort_by_value(item):
        return item[1]
    
    sorted_char_list = sorted(char_dict.items(), key=sort_by_value, reverse=True) #list of tuples
    sorted_char_dict = dict(sorted_char_list)
    return sorted_char_dict

def generate_char_count_report(char_dict: dict) -> str:
    char_report = ""
    for char in char_dict:
        line = f"The '{char}' character was found {char_dict[char]} times"
        char_report += line + "\n"
    return char_report

def generate_text_report(path: str, word_count: int, char_count: dict) -> str:
    header = f"--- Begin report of {path} ---" + "\n"
    word_count_report = f"{word_count} words found in the document" + 2*"\n"
    char_report = generate_char_count_report(char_count)
    footer = "--- End report ---"
    report = header + word_count_report + char_report + footer
    return report

main()