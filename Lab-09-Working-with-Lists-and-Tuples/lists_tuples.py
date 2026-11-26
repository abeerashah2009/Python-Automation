# Task 1: create and print a list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("The list of fruits is:", fruits)

# Task 2: modify the list
fruits.append("fig")
print("After adding 'fig':", fruits)

fruits.remove("date")
print("After removing 'date':", fruits)

fruits.sort()
print("The sorted list of fruits is:", fruits)

# Task 3: tuples are immutable
fruit_tuple = ("apple", "banana", "cherry", "elderberry", "fig")
print("The tuple is:", fruit_tuple)

try:
    fruit_tuple[0] = "avocado"
except TypeError as e:
    print(f"TypeError caught: {e}")
