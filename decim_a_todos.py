def decim_to_bin(num):
    resultado = ""
    while num >= 2:
        resto = num % 2
        num = num // 2
        resto = str(resto)
        resultado += resto
    if num == 1:
        resultado += "1"
    else:
        resultado += "0"
    if len(resultado) < 8:
        cant = 8 - len(resultado)
        resultado += "0" * cant
    result = resultado[::-1] 
    return result

def decim_to_octal(num):
    octal = ""
    while num > 0:
        residuo = num % 8
        octal = str(residuo) + octal
        num = int(num / 8)
    return octal

def decim_to_hexa(num):
    def obtener_caracter_hexadecimal(valor):
        valor = str(valor)
        equivalencias = {"10": "A", "11": "B", "12": "C", "13": "D", "14": "E", "15": "F"}
        if valor in equivalencias:
            return equivalencias[valor]
        else:
            return valor
    hexa = ""
    while num > 0:
        residuo = num % 16
        caracter = obtener_caracter_hexadecimal(residuo)
        hexa = caracter + hexa
        num = int(num / 16)
    return hexa