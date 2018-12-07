count={}
count[1]=3
count[2]=3
count[3]=5
count[4]=4
count[5]=4
count[6]=3
count[7]=5
count[8]=5
count[9]=4
count[10]=3
count[11]=6
count[12]=6
count[13]=8
count[14]=8
count[15]=7
count[16]=7
count[17]=9
count[18]=8
count[19]=8
count[20]=6
count[30]=6
count[40]=5
count[50]=5
count[60]=5
count[70]=7
count[80]=6
count[90]=6
count[100]=7
count[1000]=8
count[0]=0

letter_count=0
ten_place=0
one_place=0
for i in range(1,1001):
    if i < 21 and i > 0:
        letter_count=letter_count+count[i]
    elif i > 20 and i < 100:
        one_place = i % 10
        ten_place= i - one_place
        letter_count=letter_count+ count[ten_place]+count[one_place]
    elif i > 100 and i < 1000:
        one_place= i % 10
        ten_place= i % 100 - one_place
        hundred_place= i // 100
        print(i,one_place,ten_place,hundred_place)
        if one_place == 0 and ten_place == 0:
            letter_count = letter_count + count[hundred_place] + count[100]
        elif ten_place==10 and ten_place !=0:
            letter_count = letter_count + count[hundred_place] + count[100] + count[ i % 100] + 3
        else:
            letter_count = letter_count + count[hundred_place] + count[100] + count[ten_place] + count[one_place]+3
    else:
        letter_count=letter_count+11

print(letter_count)



