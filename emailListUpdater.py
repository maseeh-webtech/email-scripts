import subprocess
import pandas as pd

yearMapper = {
        "Freshman": 2023,
        "Sophomore": 2022,
        "Junior": 2021,
        "Senior": 2020,
        "Graduate": 2020
        }

def main():

    fileName = "roster021920.csv"
    roster = pd.read_csv(fileName)[["kerberos", "firstname", "lastname", "room", "year"]]
    if roster.isnull().values.any():
        print(roster[pd.isnull(roster["kerberos"])])
        print(roster[pd.isnull(roster["room"])])
        print(roster[pd.isnull(roster["year"])])
        print("Missing values in dataframe, see dump above")
        return

    clearLists(["maseeh-{}-private".format(year) for year in yearMapper.values()])
    addYearLists(roster)

    clearLists(["maseeh{}-freshmen".format(floor) for floor in range(7)])
    addFroshLists(roster)

def clearLists(lists):
    """Clears all members from email lists it is given"""
    for listName in lists:
        print("Clearing {}".format(listName))
        cmd = ["blanche", "-m", listName]
        memberBytes = subprocess.check_output(cmd)
        members = memberBytes.decode("utf-8").split("\n")[:-1]

        for member in members:
            cmd = ["blanche", listName, "-d", str(member)]
            res = subprocess.call(cmd)
            if res == 0:
                print("Removed {} from {}".format(member, listName))
            else:
                print("Error running command: {}".format(cmd))

def addYearLists(roster):
    """
    Adds members to their year's list (maseeh-yyyy-private) based on yearMapper 
    and their listed year.
    Currently, requires a CSV with columns kerberos, firstname, lastname, room, year.
    """
    for _, row in roster.iterrows():
        listName = "maseeh-{}-private".format(yearMapper[row.year])
        cmd = ["blanche", listName, "-a", row.kerberos]
        res = subprocess.call(cmd)
        if res == 0:
            print("Added {} to {}".format(row.kerberos, listName))
        else:
            print("Error running command: {}".format(cmd))

def addFroshLists(roster):
    """
    Add to per-floor freshman lists (maseehN-freshmen)
    Currently, requires a CSV with columns kerberos, firstname, lastname, room, year
    """
    freshmen = roster[roster["year"] == "Freshman"]
    for _, row in freshmen.iterrows():
        floor = int(row.room[-4:]) // 1000
        listName = "maseeh{}-freshmen".format(floor)
        cmd = ["blanche", listName, "-a", row.kerberos]
        res = subprocess.call(cmd)
        if res == 0:
            print("Added {} to {}".format(row.kerberos, listName))
        else:
            print("Error running command: {}".format(cmd))


if __name__ == "__main__":
    main()

