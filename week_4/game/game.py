import random

# Prompt again
while True:
    try:
        # Prompts the user for a level (n)
        n = int(input("Level: "))

    # continue if user not input a number
    except ValueError:
        continue

    # Prompt again if the user does not input a positive integer
    if n > 0:
        # Randomly generates an integer between 1 and n
        n = random.randint(1, n)
        # print(n) for trial

        # Prompt again
        while True:
            try:
                # Prompts the user to guess that integer
                g = int(input("Guess: "))

            # continue if user not input a number
            except ValueError:
                continue

            # Prompt again if the user does not input a positive integer
            if g > 0:
                # If the guess is smaller than that integer
                if  g < n:
                    # the program should output Too small!
                    print("Too small!")
                # If the guess is larger than that integer
                elif g > n:
                    # the program should output Too large!
                    print("Too large!")
                # If the guess is the same as that integer
                elif g == n:
                    # the program should output Just right!
                    print("Just right!")
                    # and exit
                    quit()
