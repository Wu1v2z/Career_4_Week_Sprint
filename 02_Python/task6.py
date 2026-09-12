cel = input('Enter a number: ')
C = float(cel)
fah = (C * 9/5) + 32

def convert_temperature(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

fah = convert_temperature(C)
print(fah)

