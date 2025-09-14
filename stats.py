def count_words(text):
    words = 0
    for _ in text.split():
        words += 1
    return words

def get_book_text(file_path):
    text = ""
    with open(file_path) as f:
        text = f.read()
    return text

def get_characters(text):
    characters = {}
    lower_text = text.lower()
    for c in lower_text:
        if c in characters:
            characters[c] += 1
        else:
            characters[c] = 1
    return characters

def get_sorted_char_list(char_dict):
    char_list = []
    for c in char_dict:
        char_list.append(
            {
                "char": c,
                "num": char_dict[c]
            }
        )
    char_list.sort(key=sort_on, reverse=True)
    return char_list

def sort_on(d):
    return d["num"]

def get_report(path):
    text = get_book_text(path)
    words = count_words(text)
    characters_dict = get_characters(text)
    sorted_list = get_sorted_char_list(characters_dict)
    print("============ BOOKBOT ============")
    print(f'Analyzing book found at {path}...')
    print('----------- Word Count ----------')
    print(f'Found {words} total words')
    print('--------- Character Count -------')
    for row in sorted_list:
        if row["char"].isalpha():
            print(f'{row["char"]}: {row["num"]}')
    print('============= END ===============')

