from stats import count_words
from stats import count_characters
from stats import word_sort

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return (file_contents)

def main():
    word_library = {}
    sorted_words = []
    book_text = get_book_text("books/frankenstein.txt")
    count_word = count_words(book_text)
    word_library = count_characters(book_text)
    sorted_words = word_sort(word_library)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {count_word} total words")
    print("--------- Character Count -------")

    
    for sort in sorted_words:
        letter = sort["char"]
        count = sort["num"]
        if letter.isalpha():
            print(f"{letter}: {count}")
        else:
            None
            
    print("============= END ===============")
    


main()
    