def get_book_text (path_to_file):
    with open(path_to_file) as f:
        return f.read()

def get_num_words(path):
    text = f"{get_book_text (path)}"
    words = text.split()
    num_words = len(words)
    print (f"Found {num_words} total words")

def dictionary(path):
    characters = {}
    text = f"{get_book_text (path)}"
    lower_text = text.lower()
    list_of_characters = list(lower_text)
    for ch in  list_of_characters:
        if f"{ch}" in characters:
            characters[f"{ch}"] += 1
        else:
            characters[f"{ch}"] = 1
    return characters 

def get_report(path):
    list_of_dictionaries = []
    dict = dictionary(path)
    for char in dict:
        num = dict[char]
        list_of_dictionaries.append( { "char" : f"{char}", "num" : num })
    def sort_on(items):
        return items["num"]
    list_of_dictionaries.sort(reverse=True, key=sort_on)
    for x in list_of_dictionaries:
        if f"{x["char"]}".isalpha() == True: 
            print (f"{x["char"]}: {x["num"]}")
