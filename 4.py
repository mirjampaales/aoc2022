#f = open("pairs_tiny.txt")
f = open('pairs.txt')

fully_contain_count = 0
overlap_count = 0

for row in f:
    elves = row.split(',')
    first = elves[0].strip()
    second = elves[1].strip()

    f_start = int(first.split('-')[0])
    f_end = int(first.split('-')[1])
    s_start = int(second.split('-')[0])
    s_end = int(second.split('-')[1])

    f_assignment = set(list(range(f_start, f_end+1)))
#    print('first ' + str(f_assignment))
    s_assignment = set(list(range(s_start, s_end+1)))
 #   print('second ' + str(s_assignment))

    smaller = min(len(f_assignment), len(s_assignment))

    overlap = f_assignment.intersection(s_assignment)
  #  print('overlap ' + str(overlap))
   # print(len(overlap))


    if len(overlap) == smaller:
        fully_contain_count += 1

    #    print('found one!')

    if len(overlap) > 0:
        overlap_count += 1

print(fully_contain_count)
print(overlap_count)