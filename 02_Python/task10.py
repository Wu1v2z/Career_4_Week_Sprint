while True:
    print('1 - hello')
    print('2 - show time')
    print('3 - exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        print('Hello!')
    elif choice == '2':
        from datetime import datetime
        now = datetime.now()
        print('Current time:', now.strftime('%Y-%m-%d %H:%M:%S'))
    elif choice == '3':
        print('Exiting the program.')
        break
    else:
        print('Invalid choice. Please try again.')
