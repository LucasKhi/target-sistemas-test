def inverter_string(s):
    string_invertida = ''
    
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]  
    
    return string_invertida

entrada = input("Digite uma string: ")

resultado = inverter_string(entrada)

print(f"A string invertida é: {resultado}")