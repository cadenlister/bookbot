def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return (file_contents)
    
def count_words(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    return count

def main():
    book_text = get_book_text("books/frankenstein.txt")
    count = count_words(book_text)
    print (f"{count} words found in the document")

main()
    