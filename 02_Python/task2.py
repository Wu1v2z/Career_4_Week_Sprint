a = input('Enter a number: ')
b = input('Enter another number: ')
d = input('Enter a third number: ')

x = int(a)
y = int(b)
z = int(d)

if x > y and x > z:
    print('The largest number is:', x)
elif y > x and y > z:
    print('The largest number is:', y)
else: 
    print('The largest number is:', z)

    