def main():
    text = input("Text: ")
    words = separate_words(text) # list
    word_counts = count_words(words) # dict
    print_word_counts(word_counts)

def separate_words(text):
    return text.split(' ')

def count_words(words):
    word_counts = {}

    for word in words:
        count = 0
        for place in words:
            if word == place:
                count += 1
        word_counts.update({word:count})

    return word_counts

def print_word_counts(word_counts):
    for key in word_counts.keys():
        print(f"{key} - {word_counts[key]}",end='\n')

if __name__ == '__main__':
    main()