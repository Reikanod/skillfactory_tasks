text = """Иванов О. 4
Петров И. 3
Дмитриев Н. 2
Смирнова О. 4
Керченских В. 5
Котов Д. 2
Бирюкова Н. 1
Данилов П. 3
Аранских В. 5
Лемонов Ю. 2
Олегова К. 4"""

with open(r'additional_files\names.txt', 'w') as f:
    f.write(text)

with open(r'additional_files\names.txt', 'r') as f:
    for line in f:
        tmpLine = line.strip()
        if int(tmpLine[-1]) < 3:
            print(line, end= "")