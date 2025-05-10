def sort_by_num(dict):
    return dict["num"]

def get_num_words(text):
    words = text.split()
    number_of_words = len(words)
    return number_of_words

def count_characters(text):
    words = text.split()
    characters = {}
    for word in words:
        word = word.lower()
        for character in word:
            if character in characters:
                characters[character] += 1
            else:
                characters[character] = 1
    return characters

def list_characters(characters):
    character_list = list()
    for character in characters:
        character_list.append({"char": character, "num": characters[character]})
    character_list.sort(reverse=True, key=sort_by_num)
    return character_list