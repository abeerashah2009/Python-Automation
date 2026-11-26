def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

def min_max(numbers):
    return min(numbers), max(numbers)

def main():
    greeting1 = greet("Alice")
    greeting2 = greet("Bob")
    print(greeting1)
    print(greeting2)
    print(greet("Carol", "Hi"))
    low, high = min_max([3, 9, 1, 7])
    print(low, high)

if __name__ == '__main__':
    main()
