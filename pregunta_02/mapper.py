#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import csv

with open('credit.csv', 'r') as file:
    content = csv.reader(file)

    for row in content:
        print(f'{row[3]},{row[4]}')