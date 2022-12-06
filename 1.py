f = open("calories.txt")
sums = [] #list of the sums of calories for each elf
cal = [] #a tiny disposable list of calories
for row in f:
    if row != '\n': #we found a row with something
        #lose the newrow and turn it to integer
        c = int(row.strip())
        #add to list of calories
        cal.append(c)
    else:
        #we found an empty row! sum what we have
        s = sum(cal)
        #add sum to the list of sums
        sums.append(s)
        #print('pow!')
        #empty the disposable list to start over
        cal = []
f.close()

#is it nice?
print(sums)
#reorder to find top three
sums.sort(reverse=True)

print(max(sums))

print(sums[0]+sums[1]+sums[2])