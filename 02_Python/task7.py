arr = []
while True:
    num = input('Enter a number (or type "done" to finish): ')
    if num.lower() == 'done':
        break
    try:
        arr.append(int(num))
    except ValueError:
        print('Please enter a valid integer or "done".')

x = sum(arr)
y = len(arr)

if y == 0:
    print('No numbers were entered.')
else:
    print('The average is:', x / y)