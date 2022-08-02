import random
import string

wins = 0
losses = 0
print("H A N G M A N\n")


def play():
    poss_answers = ["python", "java", "swift", "javascript"]
    answer = random.choice(poss_answers)
    text = "-" * len(answer)
    letters = set(answer)
    found = set({})
    attempts = 8
    while attempts != 0:
        print(text)
        guess = input("Input a letter: ")
        if len(guess) != 1:
            print("Please, input a single letter.")
        elif guess not in string.ascii_lowercase:
            print("Please, enter a lowercase letter from the English alphabet.")
        else:
            if guess not in found:
                if guess in letters:
                    found.add(guess)
                    temp = list(text)
                    for i in range(len(answer)):
                        if guess == answer[i]:
                            temp[i] = guess
                    text = "".join(temp)
                else:
                    print("That letter doesn't appear in the word.")
                    attempts -= 1
            else:
                print("You've already guessed this letter.")
        print("")
        if text == answer:
            print(f"You guessed the word {answer}!")
            print("You survived!")
            global wins
            wins += 1
            break
    else:
        print("You lost!")
        global losses
        losses += 1
    print("Thanks for playing!")


def results():
    global wins
    global losses
    print("You won:", wins, "times")
    print("You lost:", losses, "times")


while True:
    print("Type \"play\" to play the game, \"results\" to show the scoreboard, and \"exit\" to quit:")
    option = str(input())
    if option == "play":
        play()
    elif option == "results":
        results()
    elif option == "exit":
        break



