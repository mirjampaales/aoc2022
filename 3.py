import string

def item_value(item):
    #create a list of all the letters
    alphabet = list(string.ascii_letters)
    #return the index+1 number of the input
    return alphabet.index(item) + 1

#f = open("rucksacks_tiny.txt")
f = open("rucksacks.txt")

priorities = []

for row in f:
    #print(row)
    #lets find out the size of a rucksack using line length
    size = int(len(row.strip())/2)

    #separate items to two rucksacks
    #turn the list into set because sets <3
    first = set(row[:size])
    second = set(row[size:])

    #intersection of sets gives us the set of shared items
    shared = first.intersection(second)
    #back to list
    shared = list(shared)
    #take the first item from that list, turn it into string
    shared = str(shared[0])

    #get the priority of the shared item and add it to priorities list
    priorities.append(item_value(shared))

f.close()

print(sum(priorities))
