## Convertendo Graus Celsiu em Fahrenheit

def convertFahrenheit(c):
    return(c*9.5)+32

def main():
    try:
        cel = float(input('Digite a temperatura em graus Celsius: '))
        far = convertFahrenheit(cel)
        print(f"{cel} °C é igual a {far} Fahrenheit")
    except ValueError:
        print('Digite um valor valido')

if __name__ == "__main__":
    main()