from stats import count_words,count_chars
import sys

def get_book_text(the_way):
    with open(the_way,"r",encoding="utf-8") as fd:
        reading = fd.readlines()
        book_text_format = " ".join(reading)
        #print(type(book_text_format))
    return book_text_format

def banner(y,z):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {y} total words")
    print("--------- Character Count -------")
    for i in z:
        print(f"{i}: {z[i]}")

def __main__():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    the_way = sys.argv[1]
    x = get_book_text(the_way)
    y = count_words(x)
    z = count_chars(x)
    banner(y,z)


__main__()