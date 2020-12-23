import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def translate(w):
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        check = input("Did you mean %s instead?" % get_close_matches(w, data.keys())[0])
        if check == "Y" or check == "y":
            return translate(get_close_matches(w, data.keys())[0])
        else:
            return 0
    else:
        return "The word doesn't exist. Please double check it"


word = input("Enter Word: ")
word = word.lower()

meanings = translate(word)
if type(meanings) == list:
    for meaning in meanings:
        print(meaning)
else:
    print(meanings)