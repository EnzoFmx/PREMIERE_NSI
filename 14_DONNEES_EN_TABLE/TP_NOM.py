import csv
t = []
file = open('table_pokedex.csv', 'r')
d = csv.DictReader(file,delimiter=',')
for i in d :
    t.append(dict(i))
file.close()
