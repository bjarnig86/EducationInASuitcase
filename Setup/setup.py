import json
import requests

TEMP_DATA = [
    {
        "name": "ABCBurkina",
        "total_mill_smileys": 0,
        "no_mill_smiley_earned": 0,
        "active": 1,
        "issued_qr": 0,
        "sold_tablets": 0,
        "no_accounts": 25,
        "no_delivered_tablets": 5,
        "no1m_acc_rate": 0.0,
        "sold_delivered_rate": 0.0,
        "avail_tablets": 5,
        "unused_accounts": 24,
        "no_kcse_complete": 0
    },
    {
        "name": "BilalLib",
        "total_mill_smileys": 0,
        "no_mill_smiley_earned": 0,
        "active": 4,
        "issued_qr": 0,
        "sold_tablets": 0,
        "no_accounts": 50,
        "no_delivered_tablets": 15,
        "no1m_acc_rate": 0.0,
        "sold_delivered_rate": 0.0,
        "avail_tablets": 15,
        "unused_accounts": 46,
        "no_kcse_complete": 0
    },
    {
        "name": "BillianSoM",
        "total_mill_smileys": 64,
        "no_mill_smiley_earned": 16,
        "active": 100,
        "issued_qr": 9,
        "sold_tablets": 9,
        "no_accounts": 125,
        "no_delivered_tablets": 15,
        "no1m_acc_rate": 12.8,
        "sold_delivered_rate": 60.0,
        "avail_tablets": 6,
        "unused_accounts": 25,
        "no_kcse_complete": 0
    },
    {
        "name": "Chelezo",
        "total_mill_smileys": 9,
        "no_mill_smiley_earned": 4,
        "active": 28,
        "issued_qr": 4,
        "sold_tablets": 4,
        "no_accounts": 30,
        "no_delivered_tablets": 10,
        "no1m_acc_rate": 13.3,
        "sold_delivered_rate": 40.0,
        "avail_tablets": 6,
        "unused_accounts": 2,
        "no_kcse_complete": 0
    },
    {
        "name": "Harvest",
        "total_mill_smileys": 74,
        "no_mill_smiley_earned": 46,
        "active": 116,
        "issued_qr": 44,
        "sold_tablets": 44,
        "no_accounts": 200,
        "no_delivered_tablets": 60,
        "no1m_acc_rate": 23.0,
        "sold_delivered_rate": 73.3,
        "avail_tablets": 16,
        "unused_accounts": 84,
        "no_kcse_complete": 47
    },
    {
        "name": "KCRCLib",
        "total_mill_smileys": 50,
        "no_mill_smiley_earned": 18,
        "active": 46,
        "issued_qr": 5,
        "sold_tablets": 5,
        "no_accounts": 50,
        "no_delivered_tablets": 30,
        "no1m_acc_rate": 36.0,
        "sold_delivered_rate": 16.7,
        "avail_tablets": 25,
        "unused_accounts": 4,
        "no_kcse_complete": 14
    },
    {
        "name": "KakumaLib",
        "total_mill_smileys": 55,
        "no_mill_smiley_earned": 35,
        "active": 74,
        "issued_qr": 15,
        "sold_tablets": 15,
        "no_accounts": 100,
        "no_delivered_tablets": 35,
        "no1m_acc_rate": 35.0,
        "sold_delivered_rate": 42.9,
        "avail_tablets": 20,
        "unused_accounts": 26,
        "no_kcse_complete": 15
    },
    {
        "name": "Kibirichia",
        "total_mill_smileys": 0,
        "no_mill_smiley_earned": 0,
        "active": 6,
        "issued_qr": 0,
        "sold_tablets": 0,
        "no_accounts": 25,
        "no_delivered_tablets": 0,
        "no1m_acc_rate": 0.0,
        "sold_delivered_rate": 0,
        "avail_tablets": 0,
        "unused_accounts": 19,
        "no_kcse_complete": 0
    },
    {
        "name": "KongoniLib",
        "total_mill_smileys": 102,
        "no_mill_smiley_earned": 68,
        "active": 129,
        "issued_qr": 70,
        "sold_tablets": 70,
        "no_accounts": 149,
        "no_delivered_tablets": 85,
        "no1m_acc_rate": 45.6,
        "sold_delivered_rate": 82.4,
        "avail_tablets": 15,
        "unused_accounts": 20,
        "no_kcse_complete": 60
    },
    {
        "name": "MadoyaSoH",
        "total_mill_smileys": 37,
        "no_mill_smiley_earned": 15,
        "active": 64,
        "issued_qr": 15,
        "sold_tablets": 15,
        "no_accounts": 99,
        "no_delivered_tablets": 27,
        "no1m_acc_rate": 12.5,
        "sold_delivered_rate": 61.0,
        "avail_tablets": 10,
        "unused_accounts": 37,
        "no_kcse_complete": 0
    },
    {
        "name": "MajengoSoH",
        "total_mill_smileys": 42,
        "no_mill_smiley_earned": 11,
        "active": 56,
        "issued_qr": 9,
        "sold_tablets": 8,
        "no_accounts": 99,
        "no_delivered_tablets": 22,
        "no1m_acc_rate": 11.1,
        "sold_delivered_rate": 40.0,
        "avail_tablets": 12,
        "unused_accounts": 43,
        "no_kcse_complete": 1
    },
    {
        "name": "MashimoniSoH",
        "total_mill_smileys": 317,
        "no_mill_smiley_earned": 89,
        "active": 292,
        "issued_qr": 77,
        "sold_tablets": 79,
        "no_accounts": 337,
        "no_delivered_tablets": 109,
        "no1m_acc_rate": 24.9,
        "sold_delivered_rate": 79.0,
        "avail_tablets": 21,
        "unused_accounts": 45,
        "no_kcse_complete": 43
    },
    {
        "name": "MathareMCE",
        "total_mill_smileys": 46,
        "no_mill_smiley_earned": 28,
        "active": 99,
        "issued_qr": 15,
        "sold_tablets": 15,
        "no_accounts": 111,
        "no_delivered_tablets": 30,
        "no1m_acc_rate": 22.8,
        "sold_delivered_rate": 57.4,
        "avail_tablets": 15,
        "unused_accounts": 12,
        "no_kcse_complete": 0
    },
    {
        "name": "NLAFnakuru",
        "total_mill_smileys": 2,
        "no_mill_smiley_earned": 0,
        "active": 43,
        "issued_qr": 0,
        "sold_tablets": 0,
        "no_accounts": 50,
        "no_delivered_tablets": 15,
        "no1m_acc_rate": 0.0,
        "sold_delivered_rate": 0.0,
        "avail_tablets": 15,
        "unused_accounts": 7,
        "no_kcse_complete": 0
    },
    {
        "name": "RukiiraLib",
        "total_mill_smileys": 29,
        "no_mill_smiley_earned": 14,
        "active": 50,
        "issued_qr": 7,
        "sold_tablets": 7,
        "no_accounts": 99,
        "no_delivered_tablets": 20,
        "no1m_acc_rate": 14.1,
        "sold_delivered_rate": 35.0,
        "avail_tablets": 13,
        "unused_accounts": 50,
        "no_kcse_complete": 4
    },
    {
        "name": "SOSBDar",
        "total_mill_smileys": 7,
        "no_mill_smiley_earned": 5,
        "active": 32,
        "issued_qr": 1,
        "sold_tablets": 7,
        "no_accounts": 50,
        "no_delivered_tablets": 30,
        "no1m_acc_rate": 10.0,
        "sold_delivered_rate": 16.7,
        "avail_tablets": 25,
        "unused_accounts": 18,
        "no_kcse_complete": 1
    },
    {
        "name": "ShivangaLib",
        "total_mill_smileys": 1,
        "no_mill_smiley_earned": 0,
        "active": 21,
        "issued_qr": 3,
        "sold_tablets": 0,
        "no_accounts": 50,
        "no_delivered_tablets": 10,
        "no1m_acc_rate": 0.0,
        "sold_delivered_rate": 0.0,
        "avail_tablets": 10,
        "unused_accounts": 29,
        "no_kcse_complete": 0
    },
    {
        "name": "SilverSpSoH",
        "total_mill_smileys": 16,
        "no_mill_smiley_earned": 5,
        "active": 25,
        "issued_qr": 1,
        "sold_tablets": 1,
        "no_accounts": 25,
        "no_delivered_tablets": 10,
        "no1m_acc_rate": 20.0,
        "sold_delivered_rate": 10.0,
        "avail_tablets": 9,
        "unused_accounts": 0,
        "no_kcse_complete": 2
    },
    {
        "name": "StJohnsShinoyi",
        "total_mill_smileys": 0,
        "no_mill_smiley_earned": 0,
        "active": 27,
        "issued_qr": 2,
        "sold_tablets": 0,
        "no_accounts": 100,
        "no_delivered_tablets": 10,
        "no1m_acc_rate": 0.0,
        "sold_delivered_rate": 0.0,
        "avail_tablets": 10,
        "unused_accounts": 73,
        "no_kcse_complete": 0
    },
    {
        "name": "TakkOyugis",
        "total_mill_smileys": 14,
        "no_mill_smiley_earned": 10,
        "active": 14,
        "issued_qr": 1,
        "sold_tablets": 4,
        "no_accounts": 25,
        "no_delivered_tablets": 15,
        "no1m_acc_rate": 40.0,
        "sold_delivered_rate": 26.7,
        "avail_tablets": 11,
        "unused_accounts": 13,
        "no_kcse_complete": 10
    },
    {
        "name": "TaniaCentre",
        "total_mill_smileys": 127,
        "no_mill_smiley_earned": 49,
        "active": 149,
        "issued_qr": 7,
        "sold_tablets": 9,
        "no_accounts": 188,
        "no_delivered_tablets": 15,
        "no1m_acc_rate": 26.1,
        "sold_delivered_rate": 60.0,
        "avail_tablets": 6,
        "unused_accounts": 39,
        "no_kcse_complete": 35
    },
    {
        "name": "YusraSecondary",
        "total_mill_smileys": 0,
        "no_mill_smiley_earned": 0,
        "active": 8,
        "issued_qr": 0,
        "sold_tablets": 0,
        "no_accounts": 50,
        "no_delivered_tablets": 5,
        "no1m_acc_rate": 0.0,
        "sold_delivered_rate": 0.0,
        "avail_tablets": 5,
        "unused_accounts": 42,
        "no_kcse_complete": 0
    },
    {
        "name": "knlsBuruburu",
        "total_mill_smileys": 3,
        "no_mill_smiley_earned": 1,
        "active": 20,
        "issued_qr": 0,
        "sold_tablets": 0,
        "no_accounts": 25,
        "no_delivered_tablets": 5,
        "no1m_acc_rate": 4.0,
        "sold_delivered_rate": 0.0,
        "avail_tablets": 5,
        "unused_accounts": 5,
        "no_kcse_complete": 1
    },
    {
        "name": "knlsGarissa",
        "total_mill_smileys": 0,
        "no_mill_smiley_earned": 0,
        "active": 15,
        "issued_qr": 0,
        "sold_tablets": 0,
        "no_accounts": 25,
        "no_delivered_tablets": 5,
        "no1m_acc_rate": 0.0,
        "sold_delivered_rate": 0.0,
        "avail_tablets": 5,
        "unused_accounts": 10,
        "no_kcse_complete": 0
    },
    {
        "name": "knlsKibera",
        "total_mill_smileys": 111,
        "no_mill_smiley_earned": 49,
        "active": 139,
        "issued_qr": 56,
        "sold_tablets": 58,
        "no_accounts": 198,
        "no_delivered_tablets": 75,
        "no1m_acc_rate": 24.7,
        "sold_delivered_rate": 77.3,
        "avail_tablets": 17,
        "unused_accounts": 59,
        "no_kcse_complete": 6
    },
    {
        "name": "knlsMeru",
        "total_mill_smileys": 239,
        "no_mill_smiley_earned": 83,
        "active": 118,
        "issued_qr": 104,
        "sold_tablets": 109,
        "no_accounts": 149,
        "no_delivered_tablets": 120,
        "no1m_acc_rate": 55.7,
        "sold_delivered_rate": 90.8,
        "avail_tablets": 11,
        "unused_accounts": 31,
        "no_kcse_complete": 62
    },
    {
        "name": "knlsMoyale",
        "total_mill_smileys": 409,
        "no_mill_smiley_earned": 195,
        "active": 442,
        "issued_qr": 293,
        "sold_tablets": 293,
        "no_accounts": 694,
        "no_delivered_tablets": 315,
        "no1m_acc_rate": 28.1,
        "sold_delivered_rate": 93.0,
        "avail_tablets": 22,
        "unused_accounts": 252,
        "no_kcse_complete": 144
    }
]

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
            if COLUMN_META[indexes[j]][1] == "int":
                rowDict[COLUMN_META[indexes[j]][0]] = int(row[j]) if row[j] not in SPECIAL_CASE else 0
            elif COLUMN_META[indexes[j]][1] == "float":
                rowDict[COLUMN_META[indexes[j]][0]] = row[j] if row[j] not in SPECIAL_CASE else 0
            else:
                rowDict[COLUMN_META[indexes[j]][0]] = row[j] if row[j] not in SPECIAL_CASE else 0
        currentParsed.append(rowDict)

    return TEMP_DATA

if __name__ == "__main__":
    main()

# TODO:
# Get "PREV" from database (SELECCT * FROM alltime;)
# Iterate and compare curr with prev.
#     If difference in row, update HistoryData with some math
#     Finally replace prev with curr.
