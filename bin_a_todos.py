def bin_to_decim(num):
    bina = []
    suma = 0 
    binar = num[::-1]
    for binario in binar:
        bina.append(binario)
    for i in range(0,len(binar)):
        if bina[i] != "0":
            suma += (2**i)
    return suma

def bin_to_octal(num):
    decimal = 0
    for digit in num:
        decimal = decimal * 2 + int(digit)
    octal = ""
    while decimal > 0:
        octal = str(decimal % 8) + octal
        decimal //= 8
    return octal

def bin_to_hexa(num):
    hex_digits = "0123456789ABCDEF"
    hex_num = ""
    while len(num) % 4 != 0:
        num = "0" + num
    for i in range(0, len(num), 4):
        # obtener el grupo de 4 dígitos
        binary_group = num[i:i+4]
        # convertir el grupo de 4 dígitos a hexadecimal
        decimal = 0
        for digit in binary_group:
            decimal = decimal * 2 + int(digit)
        hex_digit = hex_digits[decimal]
        # agregar el dígito hexadecimal al número hexadecimal resultante
        hex_num += hex_digit
    return hex_num
