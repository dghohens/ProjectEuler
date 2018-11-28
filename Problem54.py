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
        cardset = {}
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