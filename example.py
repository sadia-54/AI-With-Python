secret_number = 42;
num_of_guesses = 1;

user_guess = int(input("Enter a number: "))

while user_guess!=secret_number and num_of_guesses<5:
    print("Incorrect")
    user_guess = int(input("Please enter a number: "))
    num_of_guesses+=1

if user_guess == secret_number:
    print("Correct")
else:
    print("Incorrect. Game Over!")


