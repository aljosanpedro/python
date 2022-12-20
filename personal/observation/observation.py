def main():
    behaviors_options = ("act", "repeat", "describe", "listen", "respond")
    
    behaviors = record_behaviors(behaviors_options)
    behaviors_count = count_behaviors(behaviors, behaviors_options)
    print_count(behaviors_count)

def record_behaviors(behaviors_options):
    behaviors = []
    
    while (True):
        behavior = input("[act, repeat, describe, listen, respond | back, done]: ")
        behavior = behavior.strip().lower()
        
        if behavior == "done":
            break
        elif behavior == "back":
            behaviors = back_behavior(behaviors)
            continue
        
        if behavior not in behaviors_options:
            print("Command not in behavior list!")
            continue
            
        behaviors.append(behavior)
        
    return behaviors        

def back_behavior(behaviors):
    if len(behaviors) <= 0:
        print("No behaviors were recorded yet!")
        return behaviors
    
    behaviors.pop(-1)
    
    return behaviors
        
def count_behaviors(behaviors, behaviors_options):
    behaviors_count = {"act"     : 0,
                       "repeat"  : 0,
                       "describe": 0,
                       "listen"  : 0,
                       "respond" : 0}
    
    for behavior in behaviors_options:
        behaviors_count[behavior] = behaviors.count(behavior)
    
    return behaviors_count

def print_count(behaviors_count):
    print("\n---Behaviors Count---")
    for behavior in behaviors_count:
        print(f"{behavior}: {behaviors_count[behavior]}")

if __name__ == "__main__":
    main()