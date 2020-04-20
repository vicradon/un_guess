from random import randrange


def start():
    mode = input("enter mode: ")
    play_mode(mode)


def play_mode(mode):
    right_number = randrange(1, 10)
    trials = 2
    print(right_number)
    for _ in range(trials):
        user_number = int(input("select a number between 1 and 10: "))

        if right_number == user_number:
            print("You win")
            replay()
        else:
            trials -= 1
            if trials == 0:
                print("You lose")
                replay()
            else:
                print(f"You have {trials} trials left")


def replay():
    start()


start()
