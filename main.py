from stats import count_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return (file_contents)

def main():
    book_text = get_book_text("books/frankenstein.txt")
    count = count_words(book_text)
    print (f"{count} words found in the document")

main()
    