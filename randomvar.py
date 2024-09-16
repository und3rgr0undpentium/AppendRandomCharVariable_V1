import random
import string

def generate_random_variable_name(variable):
    variable = variable.upper()
    new_variable = ""
    for char in variable:
        new_variable += char + random.choice(string.ascii_lowercase)
    return new_variable

def main():
    while True:
        user_input = input("Insert the variable (type 'exit' to close): ")
        if user_input.lower() == 'exit':
            print("Exiting the program.")
            break
        new_variable = generate_random_variable_name(user_input)
        print(f"New variable name: {new_variable}")

if __name__ == "__main__":
    main()
