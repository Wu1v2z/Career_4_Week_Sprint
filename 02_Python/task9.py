
while True:
    try:
        user_input = input('Enter an integer (or "done" to finish): ')
        if user_input.lower() == 'done':
            break
        number = int(user_input)
        print(f'You entered: {number}')
    except ValueError:
        print('Please enter a valid integer or "done".')

