from sys import argv, exit
import csv

# ask for 3 line arguments

if len(argv) != 3:
    print("Usage: python dna.py data.csv sequence.txt")
    exit(1)

# open database

database = open(argv[1], "r")

# open sequence

sequence = open(argv[2], "r")
sequence = sequence.read()

# open database with the csv.reader

reader = csv.DictReader(database)
datareader = csv.reader(database)

# read headers

headers = reader.fieldnames

# iterating

datalist = []
i = 1

while i < len(headers):

    n = 0
    m = n + len(headers[i])
    most = 0
    counter = 1

    while n < len(sequence):
        if headers[i] in sequence[n:m]:
            if sequence[n:m] == sequence[n - len(headers[i]):m - len(headers[i])]:
                counter += 1
                n += len(headers[i])
                m += len(headers[i])
            else:
                counter = 1
                n += len(headers[i])
                m += len(headers[i])
            if counter > most:
                most = counter
        else:
            n += 1
            m += 1
    int(most)
    datalist.append(most)
    i += 1

match = "No match"
j = 0
k = 1
dalen = len(datalist)

for row in datareader:
    while k < len(row) - 1:
        if datalist[j] != int(row[k]):
            row.clear()
            match = "No match"
        else:
            match = row[0]
            
            if datalist[dalen - 1] != int(row[len(row) - 1]):
                match = "No match"
            j += 1
            k += 1
        
print(match)
