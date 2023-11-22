with open("output_hid.txt","rb") as file:
    data = file.read().decode()

data = data.split("\n")
hid_value = []
for i in data:
    if "HID Data:" in i:
        hid_value.append(i.replace("HID Data: ",""))

usage_id = []

for i in hid_value:
    usage_id.append(str(i[0:2])+ " " + str( i[4:6]))

map = {
    "04": "a",
    "05": "b",
    "06": "c",
    "07": "d",
    "08": "e",
    "09": "f",
    "0A": "g",
    "0B": "h",
    "0C": "i",
    "0D": "j",
    "0E": "k",
    "0F": "l",
    "10": "m",
    "11": "n",
    "12": "o",
    "13": "p",
    "14": "q",
    "15": "r",
    "16": "s",
    "17": "t",
    "18": "u",
    "19": "v",
    "1A": "w",
    "1B": "x",
    "1C": "y",
    "1D": "z",
    "1E": "1",
    "1F": "2",
    "20": "3",
    "21": "4",
    "22": "5",
    "23": "6",
    "24": "7",
    "25": "8",
    "26": "9",
    "27": "0",
    "2C": " ",
    "28": "\n",
    "2F": "{",
    "30": "}",
    "2D": "-",
    "34": "'",
    "36": ",",
    "2E": "=",
    "33": ";",
}

flag = ""
for i in usage_id:
    char = i[-2:].upper()
    if char != "00":
        if i[:2] == "00":
            flag += map[char]
        else:
            flag += map[char].upper()

print(flag)
