# -*- coding: utf-8 -*-

Dictionary = {}

from csv import reader

# open file in read mode

with open("C:\\Users\\16309\\Desktop\\TennisDataMatches\\PlayerNames.csv", 'r') as read_obj:
    # pass the file object to reader() to get the reader object
    csv_reader = reader(read_obj)
    # Iterate over each row in the csv using reader object
    for row in csv_reader:
        # row variable is a list that represents a row in csv
        Dictionary[row[0]] = []

for key in Dictionary:
    lister = []
    with open("C:\\Users\\16309\\Desktop\\TennisDataMatches\\11-19-matches.csv", 'r') as read_obj2:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj2)
        # Iterate over each row in the csv using reader object
        for row in csv_reader:
            if row[5] == key:
                lister.append(row[1])
            if row[6] == key:
                lister.append(row[1])
    Dictionary[key].append(lister)
    print(Dictionary[key][0])
    print()