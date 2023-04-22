def octal_to_decim(num):
    decimal = 0
    exponente = len(num) - 1
    for digito in num:
        decimal += int(digito) * 8 ** exponente
        exponente -= 1
    return decimal

def octal_to_bin(num):
    equivalencias = {
        '0':'000',
        '1':'001',
        '2':'010',
        '3':'011',
        '4':'100',
        '5':'101',
        '6':'110',
        '7':'111'
    }
    binario = ""
    for digito in num:
        binario += equivalencias[digito]
    if not binario:
        binario = '0'
    return binario

def octal_to_hexa(num):
    hexa_equiv = {
        '0': '0', '1': '1', '2': '2', '3': '3',
        '4': '4', '5': '5', '6': '6', '7': '7',
        '10': 'A', '11': 'B', '12': 'C', '13': 'D',
        '14': 'E', '15': 'F'
    }
    # Convertir el número octal a decimal
    decimal = 0
    for i in range(len(num)):
        decimal += int(num[i]) * 8**(len(num)-i-1)
    # Convertir el número decimal a hexadecimal
    hexa = ''
    while decimal > 0:
        residuo = decimal % 16
        hexa = hexa_equiv[str(residuo)] + hexa
        decimal //= 16
    return hexa