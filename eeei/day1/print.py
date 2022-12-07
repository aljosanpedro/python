def main():
    texts = []
    texts = assign(texts)
    print('\n'.join(text for text in texts), sep='\n')
    # to join texts in a loop: '/n'.join(loop)
    # alt loop: texts[i] for i in range(len(texts))

def assign(s):
    while(True):
        x = int(input("How many texts?: "))
        if 1 <= x <= 5:
            break
    
    for i in range(x):
        s.append(input(f"Text #{i}: "))

    return s
    
if __name__ == '__main__':
    main()