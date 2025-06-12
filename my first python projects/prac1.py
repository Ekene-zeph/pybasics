print("my first python project")
import random

def math_quiz():
    print("Welcome to Zeph's Math Quiz!")

    # Generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    # Choose a random operation
    operations = ['+', '-', '*']
    operation = random.choice(operations)

    # Ask the question
    question = f"What is {num1} {operation} {num2}? "
    user_answer = input(question)

    # Calculate the correct answer
    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2

    # Check the user's answer
    try:
        if int(user_answer) == correct_answer:
            print("Correct! 🎉")
        else:
            print(f"Wrong. The correct answer was {correct_answer}.")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    math_quiz()

