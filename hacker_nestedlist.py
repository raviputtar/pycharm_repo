if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        mylist = []
        mylist.append(name)
        mylist.append(score)
        students.append(mylist)
    students.sort(key=lambda x: x[1])
    del students[0]
    sec_large = set()
    sec_large_value = students[0][1]
    sec_large.add(students[0][0])
    for i in range(len(students)):
        if students[i][1] == sec_large_value:
            sec_large.add(students[i][0])
    for i in sorted(sec_large):
        print(i)
