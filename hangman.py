class Hangman:
    pass

print "welcome"
secret_phrase = open("secret_phrase.txt").read()

# text = open("secret_phrase.txt", "r") #tester
# print(text.read()) #tester
shown_phrase = []
wrong = []
tries=10
while tries>0:

    out = ""
    for letter in secret_phrase:
        if letter in shown_phrase:
            out = out + letter
        else:
            out = out + "_"

    if out == secret_phrase:
        print "you have guessed", secret_phrase
        break

    print "guess the word and press enter", out

    guess = raw_input()

    if guess in shown_phrase or guess in wrong:
        print "Already guessed", guess
    elif guess in secret_phrase:
        print "correct"
        shown_phrase.append(guess)
    else:
        print "incorrect, you have: ", tries, "left","\n"
        tries=tries-1
        wrong.append(guess)
if tries:
     print "you have guessed", secret_phrase
else:
    print "you did not get", secret_phrase
    print "game over"

    print

