"""Problem 54
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins;
for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example,
both players have a pair of queens, then highest cards in each hand are compared (see example 4 below);
if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards
and the last five are Player 2's cards. You can assume that all hands are valid
(no invalid characters or repeated cards), each player's hand is in no specific order,
and in each hand there is a clear winner.

How many hands does Player 1 win?
"""


from collections import Counter as count


infile = open('p054_poker.txt')
fcontent = infile.readlines()

class hand:
    def __init__(self, cards):
        self.cards = cards

    def royal_flush(self):
        match = True
        suit = self.cards[1][1]
        for i in self.cards:
            if i[1] != suit:
                match = False
                break
            if i[0] not in ['T', 'J', 'Q', 'K', 'A']:
                match = False
                break
        return match

    def straight_flush(self):
        match = True
        suit = self.cards[1][1]
        highcard = ''
        cardset = set()
        for i in self.cards:
            if i[1] != suit:
                match = False
                break
            cardset.add(i[0])
        # Checks for 5 unique cards
        if len(cardset) != 5:
            match = False
        # Check for every type of straight there can be by high card, starting with K and working down to 5.
        if 'K' in cardset:
            highcard = 'K'
            if len(cardset & {'K', 'Q', 'J', 'T', '9'}) != 5:
                match = False
        elif 'Q' in cardset:
            highcard = 'Q'
            if len(cardset & {'8', 'Q', 'J', 'T', '9'}) != 5:
                match = False
        elif 'J' in cardset:
            highcard = 'J'
            if len(cardset & {'8', '7', 'J', 'T', '9'}) != 5:
                match = False
        elif 'T' in cardset:
            highcard = 'T'
            if len(cardset & {'8', '7', '6', 'T', '9'}) != 5:
                match = False
        elif '9' in cardset:
            highcard = '9'
            if len(cardset & {'8', '7', '6', '5', '9'}) != 5:
                match = False
        elif '8' in cardset:
            highcard = '8'
            if len(cardset & {'8', '7', '6', '5', '4'}) != 5:
                match = False
        elif '7' in cardset:
            highcard = '7'
            if len(cardset & {'3', '7', '6', '5', '4'}) != 5:
                match = False
        elif '6' in cardset:
            highcard = '6'
            if len(cardset & {'3', '2', '6', '5', '4'}) != 5:
                match = False
        elif '5' in cardset:
            highcard = '5'
            if len(cardset & {'3', '2', 'A', '5', '4'}) != 5:
                match = False
        return match, highcard

    def four_of_a_kind(self):
        match = True
        cardlist = []
        highcard = ''
        fourcard = ''
        for i in self.cards:
            cardlist.append(i[0])
        carddict = dict(count(cardlist))
        for i in self.cards:
            if carddict[i[0]] == 4:
                fourcard = i[0]
            elif carddict[i[0]] == 1 and highcard == '':
                highcard = i[0]
            else:
                match = False
        return match, fourcard, highcard

    def full_house(self):
        match = True
        cardlist = []
        twocard = ''
        threecard = ''
        for i in self.cards:
            cardlist.append(i[0])
        carddict = dict(count(cardlist))
        for i in self.cards:
            if carddict[i[0]] == 3:
                threecard = i[0]
            elif carddict[i[0]] == 2 and twocard == '':
                twocard = i[0]
            else:
                match = False
        return match, threecard, twocard

    def flush(self):
        match = True
        suit = self.cards[1][1]
        for i in self.cards:
            if i[1] != suit:
                match = False
                break
        return match

    def straight(self):
        match = True
        cardset = set()
        for i in self.cards:
            cardset.add(i[0])
        # Checks for 5 unique cards
        if len(cardset) != 5:
            match = False
        # Check for every type of straight there can be by high card, starting with K and working down to 5.
        # Check for A K Q J T last, after all other checks, since there's 2 ways to make a straight with A.
        if 'K' in cardset:
            highcard = 'K'
            if len(cardset & {'K', 'Q', 'J', 'T', '9'}) != 5:
                match = False
        elif 'Q' in cardset:
            highcard = 'Q'
            if len(cardset & {'8', 'Q', 'J', 'T', '9'}) != 5:
                match = False
        elif 'J' in cardset:
            highcard = 'J'
            if len(cardset & {'8', '7', 'J', 'T', '9'}) != 5:
                match = False
        elif 'T' in cardset:
            highcard = 'T'
            if len(cardset & {'8', '7', '6', 'T', '9'}) != 5:
                match = False
        elif '9' in cardset:
            highcard = '9'
            if len(cardset & {'8', '7', '6', '5', '9'}) != 5:
                match = False
        elif '8' in cardset:
            highcard = '8'
            if len(cardset & {'8', '7', '6', '5', '4'}) != 5:
                match = False
        elif '7' in cardset:
            highcard = '7'
            if len(cardset & {'3', '7', '6', '5', '4'}) != 5:
                match = False
        elif '6' in cardset:
            highcard = '6'
            if len(cardset & {'3', '2', '6', '5', '4'}) != 5:
                match = False
        elif '5' in cardset:
            highcard = '5'
            if len(cardset & {'3', '2', 'A', '5', '4'}) != 5:
                match = False
        elif 'A' in cardset:
            highcard = 'A'
            if len(cardset & {'K', 'Q', 'J', 'T', 'A'}) != 5:
                match = False
        return match, highcard

    def three_of_a_kind(self):
        match = False
        cardlist = []
        nonmatch_list = []
        threecard=''
        for i in self.cards:
            cardlist.append(i[0])
        carddict = dict(count(cardlist))
        for i in carddict:
            if carddict[i] == 3:
                threecard = i
                match = True
            else:
                nonmatch_list.append(i)
        highcard = self.high_card(nonmatch_list)
        return match, threecard, highcard

    def two_pair(self):
        match = False
        cardlist = []
        highpair = ''
        lowpair = ''
        for i in self.cards:
            cardlist.append(i[0])
        carddict = dict(count(cardlist))
        for i in carddict:
            if carddict[i] == 2 and highpair == '':
                highpair = i
            elif carddict[i] == 2:
                lowpair = i
                match = True
            else:
                highcard = i
        if card_to_num(highpair) < card_to_num(lowpair):
            swappair = lowpair
            lowpair = highpair
            highpair = swappair
        return match, highpair, lowpair, highcard

    def one_pair(self):
        match = False
        cardlist = []
        nonmatch_list = []
        pair = ''
        for i in self.cards:
            cardlist.append(i[0])
        carddict = dict(count(cardlist))
        for j in carddict:
            if carddict[j] == 2:
                pair = j
                match = True
            else:
                nonmatch_list.append(j)
        highcard = self.high_card(nonmatch_list)
        return match, pair, highcard

    def high_card(self, cards):
        highcard = ''
        cardvalues = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
        for i in cards:
            if i[0] == 'A':
                highcard = i[0]
                break
            elif i[0] == 'K' and highcard not in cardvalues[:1]:
                highcard = i[0]
            elif i[0] == 'Q' and highcard not in cardvalues[:2]:
                highcard = i[0]
            elif i[0] == 'J' and highcard not in cardvalues[:3]:
                highcard = i[0]
            elif i[0] == 'T' and highcard not in cardvalues[:4]:
                highcard = i[0]
            elif i[0] == '9' and highcard not in cardvalues[:5]:
                highcard = i[0]
            elif i[0] == '8' and highcard not in cardvalues[:6]:
                highcard = i[0]
            elif i[0] == '7' and highcard not in cardvalues[:7]:
                highcard = i[0]
            elif i[0] == '6' and highcard not in cardvalues[:8]:
                highcard = i[0]
            elif i[0] == '5' and highcard not in cardvalues[:9]:
                highcard = i[0]
            elif i[0] == '4' and highcard not in cardvalues[:10]:
                highcard = i[0]
            elif i[0] == '3' and highcard not in cardvalues[:11]:
                highcard = i[0]
            elif i[0] == '2' and highcard == '':
                highcard = i[0]
        return highcard

    def match(self):
        matchname = 10
        matchcard1 = ''
        matchcard2 = ''
        highcard = ''
        if self.royal_flush() == True:
            matchname = 1
        elif self.straight_flush()[0] == True:
            matchname = 2
            highcard = self.straight_flush()[1]
        elif self.four_of_a_kind()[0] == True:
            matchname = 3
            matchcard1 = self.four_of_a_kind()[1]
            highcard = self.four_of_a_kind()[2]
        elif self.full_house()[0] == True:
            matchname = 4
            matchcard1 = self.full_house()[1]
            highcard = self.full_house()[2]
        elif self.flush() == True:
            matchname = 5
            highcard = self.high_card(self.cards)
        elif self.straight()[0] == True:
            matchname = 6
            highcard = self.high_card(self.cards)
        elif self.three_of_a_kind()[0] == True:
            matchname = 7
            matchcard1 = self.three_of_a_kind()[1]
            highcard = self.three_of_a_kind()[2]
        elif self.two_pair()[0] == True:
            matchname = 8
            matchcard1 = self.two_pair()[1]
            matchcard2 = self.two_pair()[2]
            highcard = self.two_pair()[3]
        elif self.one_pair()[0] == True:
            matchname = 9
            matchcard1 = self.one_pair()[1]
            highcard = self.one_pair()[2]
        else:
            matchname = 10
            highcard = self.high_card(self.cards)
        return matchname, matchcard1, matchcard2, highcard


def card_to_num(card):
    cardval = 0
    if card == 'A':
        cardval = 1
    elif card == 'K':
        cardval = 2
    elif card == 'Q':
        cardval = 3
    elif card == 'J':
        cardval = 4
    elif card == 'T':
        cardval = 5
    elif card == '9':
        cardval = 6
    elif card == '8':
        cardval = 7
    elif card == '7':
        cardval = 8
    elif card == '6':
        cardval = 9
    elif card == '5':
        cardval = 10
    elif card == '4':
        cardval = 11
    elif card == '3':
        cardval = 12
    elif card == '2':
        cardval = 13
    return cardval


def winner(match_p1, match_p2):
    if match_p1[0] < match_p2[0]:
        winner = 'p1'
    elif match_p1[0] > match_p2[0]:
        winner = 'p2'
    elif match_p1[0] == match_p2[0]:
        if card_to_num(match_p1[1]) < card_to_num(match_p2[1]):
            winner = 'p1'
        elif card_to_num(match_p1[1]) > card_to_num(match_p2[1]):
            winner = 'p2'
        elif card_to_num(match_p1[1]) == card_to_num(match_p2[1]):
            if card_to_num(match_p1[2]) < card_to_num(match_p2[2]):
                winner = 'p1'
            elif card_to_num(match_p1[2]) > card_to_num(match_p2[2]):
                winner = 'p2'
            elif card_to_num(match_p1[2]) == card_to_num(match_p2[2]):
                if card_to_num(match_p1[3]) < card_to_num(match_p2[3]):
                    winner = 'p1'
                elif card_to_num(match_p1[3]) > card_to_num(match_p2[3]):
                    winner = 'p2'
                else:
                    winner = 'tie'
    return winner


if __name__ == "__main__":
    player1wins = 0
    player2wins = 0
    for i in fcontent:
        player1hand = hand(i[:15].split())
        player2hand = hand(i[15:].split())
        winhand = winner(player1hand.match(), player2hand.match())
        print(winhand)
        print(player1hand.match())
        print(player2hand.match())
        print()
        if winhand == 'p1':
            player1wins += 1
        elif winhand == 'p2':
            player2wins += 1
    print(player1wins)
    print(player2wins)
