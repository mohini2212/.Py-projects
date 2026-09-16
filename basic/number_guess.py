import random 


def number_guessing_game():
    secret=random.randint(1,100)
    max_attempts = 7
    attempts_left = max_attempts
    low=1
    high=100

    print("-"*40)
    print("Welcome to the Number Guessing Game!")
    print("-"*40)
    print("Guess a number between 1 to 100:\n")
    print(f"You have {max_attempts} attempts.\n")
    print("-"*40)


    while attempts_left > 0:
        try:
            guess=int(input(f"Attempts{max_attempts - attempts_left +1}/{max_attempts}-> Enter your guess: "))
        except ValueError:
            print("!Error!Please enter a valid number between 1-100.")
            continue
        if guess<1 or guess>100:
          print("Number must be between 1 to 100")
          continue 
        

    
        attempts_left -=1
        if guess ==secret:
            used = max_attempts - attempts_left
            print(f"Correct the number was{secret}" )
            print(f"You guessed it in {used}attempt{'s' if used>1 else''}! ")
            break
        elif guess > secret:
            high = guess -1
            print(f"↓ Too high!", end='')
        else:
            low = guess +1
            print(f" ↑ Too low!", end='')
        if attempts_left>0:
            print(f"{attempts_left} attempt{'s' if attempts_left>1 else ''} remaining. Try a number between {low}-{high}")
        else:
            print(f"\n Out of attempts! The number was {secret}. Better luck next time!")



number_guessing_game()