def main():
    word = get_word()
    is_palindrome = check_palindrome(word)
    print("Palindrome!") if is_palindrome else print("Not a palindrome.")

def get_word():
    while(True):
        s = input("Word: ")
        if s.isalpha() and len(s) > 1:
            return s

def check_palindrome(t):
    for letter in range(len(t) // 2):
        if t[letter] != t[-abs(letter + 1)]:
            return False
    return True

if __name__ == '__main__':
    main()