with open('02_Python/text/for8task.txt', 'r', encoding='utf-8') as file:
    count = sum(1 for line in file)

print(count)