import subprocess
import csv

floor = 6
listname = 'maseeh' + str(floor) + '-freshmen'

year = 4
kerberos = 1
room = 0


with open('rostersp19.csv', 'rbU') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='\n')
    first = True
    for row in reader:
        if first:
            first = False
            continue
        if row[year] == '2022':
            if row[room][0] == str(floor):
                print(row[kerberos])
                subprocess.call(['blanche', listname, '-a', row[kerberos]])

