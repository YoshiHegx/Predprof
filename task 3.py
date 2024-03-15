with open('scientist.txt', encoding='utf8') as file:
    date = input().replace('.', '-')
    while date != 'эксперимент':
        for line in file:
            if date in line:
                line = line[:-2]
                line = list(line.split('#'))
                line[0] = line[0].split()
                print(f"Ученый {line[0][0]} {line[0][1][0]}.{line[0][2][0]}. создал препарат: {line[1]} - {line[2]}")


