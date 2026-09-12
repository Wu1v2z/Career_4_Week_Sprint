# first variable
text = input('Enter a string: ')
symbol = input('Enter a symbol: ')
count = text.count(symbol)
print('The symbol', symbol, 'occurs', count, 'times in the string.')

# second variable

text2 = input('Enter another string2: ')
symbol2 = input('Enter another symbol: ')
count2 = 0 

for char in text2:
    if char == symbol2:
        count2 += 1

print('The symbol', symbol2, 'occurs', count2, 'times in the string.')

