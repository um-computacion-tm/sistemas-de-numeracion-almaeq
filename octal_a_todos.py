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
    def a_bin(numero):
        
