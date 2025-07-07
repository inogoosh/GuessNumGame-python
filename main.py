import random as rd
def play_game():
    hidden_num = rd.randint(1, 100)
    usr_guess = int(input("Guess the Number From 1 to 100: "))
    atmpt = 1
    if usr_guess == hidden_num:
        print("You WON!")
        print("Attempt taken: 1 ")
    else:
        while usr_guess != hidden_num:
            if usr_guess > hidden_num:
                if usr_guess > 100:
                    print("Please Enter a Number less than or equal to 100.")
                print("Wrong Guess, Try smaller number")
            else:
                if usr_guess < 1:
                    print("Please Enter a Number Greater than 0.")
                print("Wrong Guess, Try larger number")
            usr_guess = int(input("Guess the Number From 1 to 100: "))
            atmpt += 1
        print("You WON!")
        print(f"Attempt taken: {atmpt}")
if __name__ == "__main__":
    play_game()

