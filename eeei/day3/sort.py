# rule: don't use .sort() or sorted()

from random import randrange
LARGEST = 100000

def main():
    size = get_size()
    integers = make_list(size)
    print("Random List: " + ', '.join(str(integer) for integer in integers))

    integers = selection_sort(integers)
    print("Sorted List: " + ', '.join(str(integer) for integer in integers))

def get_size():
    while(True):
        size = int(input("List Size: "))
        if 0 < size <= 10:
            return size

def make_list(size):
    integers = []

    for _ in range(size):
        while(True):
            integer = randrange(0,LARGEST+1)
            if integer not in integers: # check duplicate
                break
        integers.append(integer)

    return integers

def selection_sort(integers):
    for loop in range(len(integers)):
        smallest = find_smallest(integers,loop)
        integers = swap_smallest(integers,smallest,loop)
    return integers
    
def find_smallest(integers,loop):
    smallest = LARGEST
    
    # MOST IMPORTANT PART: to ignore past smallests, cut the index range!
    for index in range(loop, len(integers)):
        if integers[index] < smallest:
            smallest = integers[index]

    return smallest

def swap_smallest(integers,smallest,loop):
    # current indeces
    index_small = integers.index(smallest)
    index_swap = loop
    # current values
    int_small = integers[index_small]
    int_swap = integers[index_swap]

    # swap
    integers[index_swap] = int_small
    integers[index_small] = int_swap

    return integers

if __name__ == '__main__':
    main()    
