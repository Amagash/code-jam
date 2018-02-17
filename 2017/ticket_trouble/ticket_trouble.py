# import pandas as pd
# import pprint
# import numpy as np
# import collections
# import itertools
# import copy

file = open("A-large-practice-ticket-trouble.bin", "r")
out = open("output-large-ticket-trouble", "w")

number_test_case = int(file.readline())

liste = []
for line in file:
    liste.append(map(int, line.split()))

i = 0
for case in range(1, number_test_case + 1):
    num_friends = liste[i][0]
    grid_dim = liste[i][1]

    tickets = []
    for count in range(1, num_friends+1):
        tickets.append(liste[i+count])

    tickets.sort()

    new_tickets = list(tickets)
    for ticket in tickets:
        new_tickets.append([ticket[1], ticket[0]])

    tickets_set = [list(t) for t in set(tuple(element) for element in new_tickets)]
    tickets_set.sort()

    count = 0
    max_count = 0
    current_row = 1

    for element in tickets_set:
        if element[0] == current_row:
            count += 1
        else:
            current_row = element[0]
            count = 1
        if count > max_count:
            max_count = count
    out.write("Case #{}: {}\n".format(case, max_count))

    i += num_friends+1

file.close()
out.close()
