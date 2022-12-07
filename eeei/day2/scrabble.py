def main():
    word = get_word()
    score = calculate_score(word)
    print("Score:", score)

def get_word():
    while(True):
        s = input("Word: ")
        if s.isalpha():
            return s.upper()

def calculate_score(t):
    dict = {
        1: "AEIOULNSTR",
        2: "DG",
        3: "BCMP",
        4: "FHVWY",
        5: 'K',
        8: "JX",
        10: "QZ"
    }
    i = 0
    
    for letter in t:
        for points in dict.keys():
            if letter in dict[points]:
                i += points
    
    return i

if __name__ == '__main__':
    main()