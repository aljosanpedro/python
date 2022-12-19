def main():
    behaviors_count = {"act"     : 0,
                       "repeat"  : 0,
                       "describe": 0,
                       "listen"  : 0,
                       "respond" : 0}
    
    behaviors_count = count_behaviors(behaviors_count)
    print_count(behaviors_count)

def count_behaviors(behaviors_count):
    while (True):
        behavior = input("[act, repeat, describe, listen, respond, done, delete]: ")
        
        if behavior == "done":
            break
        
        if behavior == "delete":
            behaviors_count = delete_behavior(behaviors_count)
            continue
        
        if behavior not in behaviors_count.keys():
            print("Behavior not in list!")
            continue
            
        behaviors_count[behavior] += 1
        
    return behaviors_count

        
        
def delete_behavior(behaviors_count):
    while (True):
        behavior = input("What to delete by 1 [act, repeat, describe, listen, respond]?: ")
        
        if behavior not in behaviors_count.keys():
            print("Behavior not in list!")
            continue
            
        behaviors_count[behavior] -= 1
    
        return behaviors_count

def print_count(behaviors_count):
    for behavior in behaviors_count:
        print(f"{behavior}: {behaviors_count[behavior]}")

if __name__ == "__main__":
    main()