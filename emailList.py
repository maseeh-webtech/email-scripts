import subprocess
import csv

# test:
#a = subprocess.call(["blanche", "-a", "graceyin", "maseeh-2020"])

# column numbers in csv of residents
year = 4
kerberos = 1

with open("rostersp19.csv", "rbU") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar="\n")
    first = True
    for row in reader:
        if first:
            first = False
            continue
        if row[year] == "2019" or row[year] == "exchange": #row[year] != "2020" and row[year] != "":
            print(row[kerberos])
            res = subprocess.call(["blanche", "-a", row[kerberos], "maseeh-2019-private"])
            print(res)

