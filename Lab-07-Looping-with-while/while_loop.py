user_input = ''

try:
    while True:
        try:
            user_input = input("Enter a string (type 'exit' to quit): ")
        except EOFError:
            print("\nInput ended.")
            break

        if user_input == "exit":
            print("Exiting the loop. Goodbye!")
            break

        print("You entered:", user_input)

finally:
    print("Program terminated successfully.")
