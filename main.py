def main():
    book_path = "books\\frankenstein.txt"
    text = read_book(book_path)
    no_of_words = count_words(text)
    letter_count = count_letters(text)
    print(f"--- Begin report of {book_path} ---")
    
    resultList = list(letter_count.items())
    resultList.sort()
    print(f"--- Begin report of books/frankenstein.txt ---")
    for item in resultList:
        if item[0].isalpha():
            print(f"The {item[0]} character was found {item[1]} times")
    print("--- End report ---")


def read_book(path):
    with open(path) as f:
        return f.read()
    

def count_words(text):
    return len(text.split(' '))
    
def count_letters(text):
    words = (text.split(' '))
    dict_count_letters = {}
    for word in words:
        for i in word:
            if i.lower() in dict_count_letters:
                dict_count_letters[i.lower()] += 1
            else:
                dict_count_letters[i.lower()] = 0
    return dict_count_letters

def print_report(text):
    resultDict = count_letters(text)
    


main()