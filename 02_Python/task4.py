numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, 31, 44, 55, 66, 77, 88, 99]
even_numbers = []

for i in numbers:
    if i % 2 == 0:
        print(i, 'парне число.')
        even_numbers.append(i)
    else:
        print(i, 'непарне число.')


print('Парні числа:', even_numbers)
print('Кількість парних чисел:', len(even_numbers))
print('Не парні числа:', [i for i in numbers if i % 2 != 0])