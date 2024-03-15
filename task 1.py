answer = []
with open('scientist.txt', encoding='utf8') as file:
    for line in file:
        if 'Аллопуринол' in line:
            date = ''
            line = line[:-2]
            line = list(line.split('#'))
            date = line[2].replace('-', '')
            line = line[::-1]
            line.append(date)
            answer.append(line[::-1])
    answer = sorted(answer)
    print('Разработчиками Аллопуринола были такие люди:' '\n')
    count = 0
    while count != len(answer):
        print(f"{answer[count][1]} - {answer[count][3]}")
        count+=1
    print(f"Оригинальный рецепт принадлежит: {answer[0][1]}")
