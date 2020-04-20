from random import randrange


def init():
    print("Welcome to UnGuess, the best guessing game out there. \nPlease, enter the right input when prompted\n\n")


keep_playing = True


def level_details(mode):
    if mode == 'easy':
        return {'guesses': 6, 'range': 10, 'message': "You selected 'easy'. You have 6 trials to guess a number between 1 and 10."}
    elif mode == 'medium':
        return {'guesses': 4, 'range': 20, 'message': "You selected 'medium'. You have 4 trials to guess a number between 1 and 20."}
    else:
        return {'guesses': 3, 'range': 50, 'message': "You selected 'hard'. You have 3 trials to guess a number between 1 and 50."}


def play_game():
    mode = input(
        "Please, enter your desired mode \n(easy, medium or hard): ")
    while mode != 'easy' and mode != 'medium' and mode != 'hard':
        mode = input(
            "Please, enter a right response. Either 'easy', 'medium' or 'hard'. Must be lowercase: ")

    play_mode(mode)


def play_mode(mode):
    right_number = randrange(1, 10)
    trials = level_details(mode)['guesses']
    guess_range = level_details(mode)['range']

    while trials > 0 and keep_playing:
        user_number = None
        not_proceed = True

        while not_proceed:
            try:
                user_number = int(input(f"Select a number between 1 and {guess_range}: "))
                not_proceed = False
            except ValueError as val:
                print(f"Error! You entered {str(val).split(' ')[-1]} which is not a number")
                not_proceed = True

        if right_number == user_number:
            print("You got it right!")
            replay()
        else:
            trials -= 1
            if trials == 0:
                print("Game Over! You lose!")
                replay()
            else:
                print(f"That was wrong. \nYou have {trials} trials left")


def replay():
    replay_value = input("Do you want to play again? \n(yes or no):")
    while replay_value != 'yes' and replay_value != 'no':
        replay_value = input(
            "Please, enter 'yes' or 'no'. \nDo you want to play again?: ")
    if replay_value == 'yes':
        play_game()
    elif replay_value == 'no':
        print("Thanks for playing. See ya!")
        global keep_playing
        keep_playing = False


init()
play_game()
