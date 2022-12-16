import json
import requests

COLUMN_META = {
    "name": ("name", "string"),
    "MSMLY": ("total_mill_smileys", "int"),
    "#n1M": ("no_mill_smiley_earned", "int"),
    "active": ("active", "int"),
    "numQR": ("issued_qr", "int"),
    "#sold": ("sold_tablets", "int"),
    "#acc": ("no_accounts", "int"),
    "#del": ("no_delivered_tablets", "int"),
    "n1M%acc": ("no1m_acc_rate", "float"),
    "s%d": ("sold_delivered_rate", "float"),
    "avail": ("avail_tablets", "int"),
    "unused": ("unused_accounts", "int"),
    "#KCSE": ("no_kcse_complete", "int")
}

SPECIAL_CASE = ["NaN", "<NA>"]

def fetch_data():
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
            if COLUMN_META[indexes[j]][1] == "int":
                rowDict[COLUMN_META[indexes[j]][0]] = int(row[j]) if row[j] not in SPECIAL_CASE else 0
            elif COLUMN_META[indexes[j]][1] == "float":
                rowDict[COLUMN_META[indexes[j]][0]] = float(row[j]) if row[j] not in SPECIAL_CASE else 0
            else:
                rowDict[COLUMN_META[indexes[j]][0]] = row[j] if row[j] not in SPECIAL_CASE else 0
        currentParsed.append(rowDict)

    return currentParsed

if __name__ == "__main__":
    main()

# TODO:
# Get "PREV" from database (SELECCT * FROM alltime;)
# Iterate and compare curr with prev.
#     If difference in row, update HistoryData with some math
#     Finally replace prev with curr.
