import random

def main():
    # call function get_level()
    lvl = get_level()
    # call function game_rounds to get the points
    points = game_rounds(lvl)
    # output the points
    print(f"c: {points}")

def get_level():
    # loop until conditions are true
    while True:
        # try block
        try:
            # prompt user to input a level
            lvl = int(input("Level: "))
            # input should be between 1 to 3
            if lvl >= 1 and lvl <= 3:
                # escape the loop
                break
        # disregard all errors
        except:
            # pass and do noting
            pass
    # return the input
    return lvl

def generate_integer(lvl):
    # if input is equal to 1
    if lvl == 1:
        # assign random int to x & y from 0 to 9
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    # if input is equal to 2
    elif lvl == 2:
        # assign random int to x & y from 10 to 99
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    # if input is equal to 3
    else:
        # assign random int to x & y from 100 to 999
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    # return random ints (x & y)
    return x, y

def game_attempts(x, y):
    # set attempts equal to 1
    attempts = 1
    # continue if condition is met
    while attempts <= 3:
        # add try block to catch the error
        try:
            # assign input to solution variable
            solution = int(input(f"{x} + {y} = "))
            # if equals to x + y
            if solution == (x + y):
                return True
            else:
                # add 1 to attempts variable
                attempts += 1
                # print "EEE" as error message
                print("EEE")
        # if error
        except:
            # add 1 to attempts variable
            attempts += 1
            # print "EEE" as error message
            print("EEE")
    # show correct solution
    print(f"{x} + {y} = {x + y}")
    return False

def game_rounds(lvl):
    # assign 1 to rounds var
    rounds = 1
    # initial points is 0
    points = 0
    # check if condition is met
    while rounds <= 10:
        # assign the level to x y var
        x, y = generate_integer(lvl)
        # assign to response var
        response = game_attempts(x, y)

        # if true
        if response == True:
            # add 1 to points
            points += 1
        #add 1 to rounds
        rounds += 1
    return points

if __name__ == "__main__":
    main()