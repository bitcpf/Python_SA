#!/usr/bin/python
# Filename: while.py

number = 23
running = True

while running:
    guess = int(raw_input('Enter an integer : '))

    if guess == number:
        print 'Congratulations, you guessed it.' 
        running = False # this causes the while loop to
    elif guess < number:
        print 'No, it is a little'
    else:
        print 'No, it'
else:
    print 'The while loop is over.' 
print 'Done'
