from random import randrange

def main():
    size = get_size()
    places = make_places(size)
    
    steps = get_steps()
    final = step_places(places, steps)
    print("Final Place:", final)

def get_size():
    while(True):
        size = int(input("Size: "))
        if 4 <= size <= 36+1:
            return size

def make_place(places):
    while(True):
        place = randrange(0,36+1)
        if place in places: # check duplicate
            continue
        else:
            return place

def make_places(size):
    places = []
    for _ in range(size):
        place = make_place(places)
        places.append(place)

    places = sorted(places)
    print("Places: " + ', '.join(str(place) for place in places))

    return places

def get_steps():
    while(True):
        steps = int(input("Steps: "))
        if steps > 0:
            return steps

def step_places(places, steps):
    steps %= len(places) # remainder -> "looping index"
    return places[steps-1] # -1 because 0-index

if __name__ == '__main__':
    main()