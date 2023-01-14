def guess2():
    print('Think of a number in range 1-1000 and let me guess it in 10 tries')
    min = 0
    max = 1000
    for i in range(10):
        guess = int((max - min) / 2 + min)
        print(f"I'm guessing: {guess}")
        answer = input('If the guess is correct, type "You win". If not, type - "To small" or "To big". Your answer:')
        if answer == 'You win':
            return 'I won!'
        elif answer == 'To small':
            min = guess
        elif answer == 'To big':
            max = guess
        else:
            print("Don't cheat!")
            return guess2()
    print("Don't cheat!")
    return guess2()

print(guess2())
