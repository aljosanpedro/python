"""
static methods
- don't change any class variables or attributes
- more for organization
    - try: many methods for one function -> split into class with static methods

@staticmethod
def name(cls):
    return
"""

class Math:

    @staticmethod
    def add_5(x):
        return x + 5

    @staticmethod
    def add_10(x):
        return x + 10

    @staticmethod
    def run():
        print("run")

def main():
    Math.run() # run
    print(Math.add_5(10)) # 15
    print(Math.add_10(20)) # 30

if __name__ == "__main__":
    main()
