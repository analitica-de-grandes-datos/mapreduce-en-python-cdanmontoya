#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import csv

with open('credit.csv', 'r') as file:
    content = csv.reader(file)

    for row in content:
        mapped_value = row[2].rstrip()
        print(f'{mapped_value}')