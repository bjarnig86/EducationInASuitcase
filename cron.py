import json
import requests

COLUMN_META = {
    "name": "name",
    "MSMLY": "total_mill_smileys",
    "#n1M": "no_mill_smiley_earned",
    "active": "active",
    "numQR": "issued_qr",
    "#sold": "sold_tablets",
    "#acc": "no_accounts",
    "#del": "no_delivered_tablets",
    "n1M%acc": "no1m_acc_rate",
    "s%d": "sold_delivered_rate",
    "avail": "avail_tablets",
    "unused": "unused_accounts",
    "#KCSE": "no_kcse_complete",
}

def fetch_data():
    # lines = []
    # with open('lib.txt') as f:
    #     lines = f.readlines()
    # return lines
    response = requests.get("https://libraries.tutor-web.net/tables/alltime.1M.txt")
    return response.text.strip().split("\n")

def printAsJson(data):
    print(json.dumps(data, indent=4, ensure_ascii=False))
    
def main():
    currentParsed = []
    indexes = ["name"]
    lines = []
    try:
        lines = fetch_data()
    except Exception as err:
        print("Error :>> ", err)

    # Iterate through each line of table
    for i in range(1, len(lines)-1):
        rowDict = {}
        # If it's the header column split it and create an array
        if i == 1:
            indexes = indexes + lines[1].split()
            continue

        # Spread line to array of data
        row = lines[i].split()

        # Iterate throgh header column and parse data to dict
        # with indexing
        for j in range(len(indexes)):
            rowDict[COLUMN_META[indexes[j]]] = row[j]
        
        currentParsed.append(rowDict)

    printAsJson(currentParsed)

if __name__ == "__main__":
    main()

# TODO:
# Fetch data from https://libraries.tutor-web.net/tables/alltime.1M.txt

# Get "PREV" from database (SELECCT * FROM alltime;)
# Iterate and compare curr with prev.
#     If difference in row, update HistoryData with some math
#     Finally replace prev with curr.
