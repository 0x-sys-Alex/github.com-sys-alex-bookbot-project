def count_words(book_text_format):
    separate_words = book_text_format.replace("\n","").split(" ")
    try:
        while True:
            separate_words.remove('')
    except:
        num_words = len(separate_words)
        return num_words

def count_chars(book_text_format):
    count = dict()
    text_for_count = book_text_format.lower()
    for i in text_for_count:
        if ord(i)>=97 and ord(i)<=122:
            if i in count:
                count[i]+=1
            else:
                count[i]=1
    return count
        

