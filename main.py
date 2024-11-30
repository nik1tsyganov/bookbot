def count_words(text):
    return len(text.split())

def count_character(text):
    lower_case_text = text.lower()
    dict_letters = {}
    for char in lower_case_text:
        dict_letters[char] = dict_letters.get(char, 0) + 1
    
    return dict_letters

def submit_report(path, num_chars, char_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{num_chars} words found in the document")
    print("\n")
    for char, freq in char_dict.items():
        if char.isalpha():
            print(f"The '{char}' character was found {freq} times")
    print("--- End report --- ")

def main():
    path_to_file = "books/frankenstein.txt"
    with open(path_to_file) as f:
        file_contents = f.read()
        submit_report(path_to_file, count_words(file_contents), count_character(file_contents))

# __name__
if __name__=="__main__":
    main()