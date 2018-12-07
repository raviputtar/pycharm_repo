card_rank = {}
card_rank["A"] = 14
card_rank["K"] = 13
card_rank["Q"] = 12
card_rank["J"] = 11
card_rank["T"] = 10

card_rank["9"] = 9
card_rank["8"] = 8
card_rank["7"] = 7
card_rank["6"] = 6
card_rank["5"] = 5
card_rank["4"] = 4
card_rank["3"] = 3
card_rank["2"] = 2



def count_Suits_of_each_type(suitlist):
    count_clubs = 0
    count_diamonds = 0
    count_hearts = 0
    count_spades = 0
    for i in suitlist:
        if i == "C":
            count_clubs = count_clubs + 1
        elif i == "D":
            count_diamonds = count_diamonds + 1
        elif i == "S":
            count_spades = count_spades + 1
        else:
            count_hearts = count_hearts + 1
    mysuitcount = dict()
    mysuitcount["C"] = count_clubs
    mysuitcount["D"] = count_diamonds
    mysuitcount["H"] = count_hearts
    mysuitcount["S"] = count_spades
    return mysuitcount


def count_card_of_same_value(card_list):
    ace_count = 0
    two_count = 0
    three_count = 0
    four_count = 0
    five_count = 0
    six_count = 0
    seven_count = 0
    eight_count = 0
    nine_count = 0
    ten_count = 0
    jack_count = 0
    queen_count = 0
    king_count = 0
    for key in card_list:
        if key == "A":
            ace_count = ace_count + 1
        if key == "2":
            two_count = two_count + 1
        if key == "3":
            three_count = three_count + 1
        if key == "4":
            four_count = four_count + 1
        if key == "5":
            five_count = five_count + 1
        if key == "6":
            six_count = six_count + 1
        if key == "7":
            seven_count = seven_count + 1
        if key == "8":
            eight_count = eight_count + 1
        if key == "9":
            nine_count = nine_count + 1
        if key == "T":
            ten_count = ten_count + 1
        if key == "J":
            jack_count = jack_count + 1
        if key == "Q":
            queen_count = queen_count + 1
        if key == "K":
            king_count = king_count + 1

    myvalue_dict = dict()
    myvalue_dict["A"] = ace_count
    myvalue_dict["2"] = two_count
    myvalue_dict["3"] = three_count
    myvalue_dict["4"] = four_count
    myvalue_dict["5"] = five_count
    myvalue_dict["6"] = six_count
    myvalue_dict["7"] = seven_count
    myvalue_dict["8"] = eight_count
    myvalue_dict["9"] = nine_count
    myvalue_dict["T"] = ten_count
    myvalue_dict["J"] = jack_count
    myvalue_dict["Q"] = queen_count
    myvalue_dict["K"] = king_count

    return myvalue_dict


myresult_list = []


def High_card(card_list):  # Highest value card
    score = 0
    global myhand_score
    high_card = 0
    mylist = []
    for key in card_list:
        if key == "J":
            mylist.append(11)
        elif key == "K":
            mylist.append(13)
        elif key == "Q":
            mylist.append(12)
        elif key == "A":
            mylist.append(14)
        elif key == "T":
            mylist.append(10)
        else:
            mylist.append(int(key))
    mylist.sort()
    high_card = mylist[4]
    score = high_card

    return score


def One_Pair(card_list):  # Two cards of the same value.
    score = 0
    c_rank = 0
    mycardvalue = dict()
    mycardvalue = count_card_of_same_value(card_list)

    for i in mycardvalue:
        if mycardvalue[i] == 2:
            c_rank = card_rank[i]
            score = c_rank
            break

    return score


def Two_Pairs(card_list):  # Two different pairs.
    score = 0
    mycardvalue = dict()
    pair_counter = 0
    mycardvalue = count_card_of_same_value(card_list)
    largest_rank = 0
    myresult_list = []
    for i in mycardvalue:
        if mycardvalue[i] == 2:
            c_rank = card_rank[i]
            if c_rank > largest_rank:
                largest_rank = c_rank
            pair_counter = pair_counter + 1
            if pair_counter == 2:
                score = largest_rank
                break
    return score


def Three_of_a_Kind(card_list):  # Three cards of the same value.
    score = 0
    global myhand_score
    mycardvalue = dict()
    mycardvalue = count_card_of_same_value(card_list)

    for i in mycardvalue:
        if mycardvalue[i] == 3:
            c_rank = card_rank[i]
            score = c_rank
            break
    return score


def Straight(card_list):  # All cards are consecutive values.
    score = 0
    mylist = []
    for key in card_list:
        if key == "J":
            mylist.append(11)
        elif key == "K":
            mylist.append(13)
        elif key == "Q":
            mylist.append(12)
        elif key == "A":
            mylist.append(14)
        elif key == "T":
            mylist.append(10)
        else:
            mylist.append(int(key))
    mylist.sort()
    if mylist[1] == mylist[0] + 1:
        if mylist[2] == mylist[1] + 1:
            if mylist[3] == mylist[2] + 1:
                if mylist[4] == mylist[3] + 1:
                    score = mylist[4]
    return score


def Flush(card_list, suitlist):  # All cards of the same suit.
    score = 0
    mysuitcount = dict()
    mysuitcount = count_Suits_of_each_type(suitlist)
    myresultlist = []
    mylist = []
    for key in card_list:
        if key == "J":
            mylist.append(11)
        elif key == "K":
            mylist.append(13)
        elif key == "Q":
            mylist.append(12)
        elif key == "A":
            mylist.append(14)
        elif key == "T":
            mylist.append(10)
        else:
            mylist.append(int(key))
    mylist.sort()
    if mysuitcount["H"] == 5 or mysuitcount["S"] == 5 or mysuitcount["D"] == 5 or mysuitcount["C"] == 5:
        score = mylist[4]
    return score


def Full_house(card_list):  # Three of a kind and a pair.
    score = 0
    Three_of_kind = False
    pair_of_card = False
    mycardvalue = dict()
    mycardvalue = count_card_of_same_value(card_list)
    myresultlist = []
    largest_rank = 0
    for s in mycardvalue:
        if mycardvalue[s] == 3:
            Three_of_kind = True
            largest_rank = card_rank[s]
            break
    for j in mycardvalue:
        if mycardvalue[j] == 2:
            pair_of_card = True
            if card_rank[j] > largest_rank:
                largest_rank = card_rank[j]
            break

    if Three_of_kind == True and pair_of_card == True:
        score = largest_rank
    return score


def Four_of_a_Kind(card_list):  # Four cards of the same value.
    score = 0
    mycardvalue = dict()
    mycardvalue = count_card_of_same_value(card_list)
    myresultlist = []
    print("four_of_Cardvalue", mycardvalue)
    for i in mycardvalue:
        if mycardvalue[i] >= 4:
            score = card_rank[i]
            break
    return score


def Straight_Flush(card_list, suitlist):  # All cards are consecutive values of same suit.
    score = 0
    mysuitcount = dict()
    mysuitcount = count_Suits_of_each_type(suitlist)
    myresultlist = []
    if mysuitcount["H"] == 5 or mysuitcount["S"] == 5 or mysuitcount["D"] == 5 or mysuitcount["C"] == 5:
        mylist = []
        for key in card_list:
            if key == "J":
                mylist.append(11)
            elif key == "K":
                mylist.append(13)
            elif key == "Q":
                mylist.append(12)
            elif key == "A":
                mylist.append(14)
            elif key == "T":
                mylist.append(10)
            else:
                mylist.append(int(key))
        mylist.sort()
        if mylist[1] == mylist[0] + 1:
            if mylist[2] == mylist[1] + 1:
                if mylist[3] == mylist[2] + 1:
                    if mylist[4] == mylist[3] + 1:
                        score = mylist[4]

    return score


def Royal_Flush(card_list, suitlist):  # Ten, Jack, Queen, King, Ace, in same suit.
    score = 0
    mysuitcount = dict()
    myresultlist = []
    mysuitcount = count_Suits_of_each_type(suitlist)
    mycardvalue = dict()
    mycardvalue = count_card_of_same_value(card_list)

    if mysuitcount["H"] == 5 or mysuitcount["S"] == 5 or mysuitcount["D"] == 5 or mysuitcount["C"] == 5:
        if mycardvalue["T"] == 1 and mycardvalue["J"] == 1 and mycardvalue["K"] == 1 and mycardvalue["Q"] == 1 and mycardvalue["A"] == 1:
            score = 10
            myhand_score[1] = 10

    return score


def get_score(p_cards, p_suits):
    pscore = dict()
    pscore[1] = Royal_Flush(p_cards, p_suits)
    pscore[2] = Straight_Flush(p_cards, p_suits)
    pscore[3] = Four_of_a_Kind(p_cards)
    pscore[4] = Full_house(p_cards)
    pscore[5] = Flush(p_cards, p_suits)
    pscore[6] = Straight(p_cards)
    pscore[7] = Three_of_a_Kind(p_cards)
    pscore[8] = Two_Pairs(p_cards)
    pscore[9] = One_Pair(p_cards)
    pscore[10] = High_card(p_cards)
    return pscore


wincount = 0


def check_winner(p1_cards, p1_suits, p2_cards, p2_suits):
    global wincount
    p1_score = {}
    p2_score = {}
    p1_score = get_score(p1_cards, p1_suits)
    print("p1_Score-->", p1_score)
    p2_score = get_score(p2_cards, p2_suits)
    print("p2_Score-->", p2_score)
    for i in range(1, 11):
        if p1_score[i] > p2_score[i]:
            wincount += 1
            print("p1 is winner by", i, "greater")
            break
        elif p1_score[i] == 0 and p2_score[i] == 0:
            pass
        elif p1_score[i] == p2_score[i]:
            pass
        else:
            print("p2 is winner by greater",i)
            break


with open("C:\\Users\\rsingh\\PycharmProjects\\euler\\p054_poker.txt") as f:
    for line in f:
        print("--------------------------")
        print(line)
        mylist = line.split(" ")
        p1_cardlist = []
        p1_suitlist = []
        p2_cardlist = []
        p2_suitlist = []
        for i in range(0, len(mylist)):
            templist = []
            if i < 5:
                templist.append(mylist[i][0:1])
                templist.append(mylist[i][1:2])
                p1_cardlist.append(templist[0])
                p1_suitlist.append(templist[1])
            else:
                templist.append(mylist[i][0:1])
                templist.append(mylist[i][1:2])
                p2_cardlist.append(templist[0])
                p2_suitlist.append(templist[1])

        check_winner(p1_cardlist, p1_suitlist, p2_cardlist, p2_suitlist)

print("p1_wins are-->", wincount)





