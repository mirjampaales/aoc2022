#f = open('signal_tiny.txt') #small testfile
f = open('signal.txt')

message = []

counter = 0

while 1:

    # read file character-by-character
    char = f.read(1)
    if not char:
        break

    #each step, we add a new character to the message we are analyzing
    message.append(char)
    """
    when we have reached the size of the message (4 or 14 characters),
    we start looking for sequences of unique characters
    """
    #if len(four_characters) == 4:  #part 1 of the puzzle
    if len(message) == 14:          #part 2 of the puzzle

        #set function removes duplicates and if the lengths match we have found it
        if len(message) == len(set(message)):
            #print('pow!')
            break

        #we have not found a sequence of unique characters, so we remove the first and start over
        else:
            message = message[1:]

    #we also need a counter to know where we are
    counter = counter + 1

    #print(str(counter) + ". character is " + char) #when testing things out this row is good. not good for the actual puzzle input :)

f.close()

#oops, I started the counter from 0, but people khm. elves don't count like that. add 1
print(counter+1)