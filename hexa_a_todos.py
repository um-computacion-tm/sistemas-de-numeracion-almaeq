def hexa_to_decim(num):
    hexa_equiv = {
        '0': 0, '1': 1, '2': 2, '3': 3,
        '4': 4, '5': 5, '6': 6, '7': 7,
        '8': 8, '9': 9, 'A': 10, 'B': 11,
        'C': 12, 'D': 13, 'E': 14, 'F': 15
    }
    decimal = 0
    for i in range(len(num)):
        decimal += hexa_equiv[num[i].upper()] * 16**(len(num)-i-1)
    return decimal

def hexa_to_bin(num):
    equivalencias = {
        "0":"0000",
        "1":"0001",
        "2":"0010",
        "3":"0011",
        "4":"0100",
        "5":"0101",
        "6":"0110",
        "7":"0111",
        "8":"1000",
        "9":"1001",
        "A":"1010",
        "B":"1011",
        "C":"1100",
        "D":"1101",
        "E":"1110",
        "F":"1111"
    }
    binario = ""
    for i in range(len(num)):
        binario += equivalencias[num[i].upper()]
    return binario

def hexa_to_octal(num):
    hexa_equiv = {"0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111",
                "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111"}
    binario = ""
    for digito in num:
        binario += hexa_equiv[digito.upper()]
    while len(binario) % 3 != 0:
        binario = "0" + binario
    octal = ""
    for i in range(0, len(binario), 3):
        grupo = binario[i:i+3]
        octal_equiv = {"000": "0", "001": "1", "010": "2", "011": "3", "100": "4", "101": "5", "110": "6", "111": "7"}
        octal += octal_equiv[grupo]
    return octal