def main():
    size = get_size()
    integers = get_integers(size)
    print("Largest Integer:", get_largest(integers))

def get_size():
    while(True):
        size = int(input("How many integers?: "))
        if 1 <= size <= 5:
            return size

def get_integers(size):
    integers = []
    for index in range(size):
        while(True): # avoid duplicates
            integer = int(input(f"Integer #{index + 1}: "))
            if integer in integers:
                print("Duplicate!")
            else:
                break
        integers.append(integer)
    return integers

def get_largest(integers):
    integers = sorted(integers, reverse=True)
    return integers[0]
    
    '''
    largest = 0
    for index in range(len(integers)):
        if integers[index] > largest:
            largest = integers[index]
    return largest
    '''
        
if __name__ == '__main__':
    main()