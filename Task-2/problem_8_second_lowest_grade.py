table = []
scores = set()
names = []


if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        table.append([name,score])
        scores.add(score)
    
    second_lowest_grade = sorted(scores)[1] 
    for i in range(len(table)):
        if table[i][1]== second_lowest_grade :
            names.append(table[i][0])
    names = sorted(names)
    for name in names :
        print(name)