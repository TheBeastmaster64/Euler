# we convert the hand the user enters into an array that is easy to compare
# it follows this format: [value of hand, most repeating card, second most repeating card, other cards]
# if two cards repeat the same amount, they are entered in decsending order
# the following lists the value of each hand:
# straight flush = 8, four of a kind = 7, full house = 6, flush = 5, straight = 4
# three of a kind = 3, two pair = 2, single pair = 1, high card = 0

from operator import itemgetter
class Poker_Hand:
    def __init__(self, hand):  # Hand is the set of 5 cards one has
        self.hand = self.processRawHand(hand)
        self.SIZE = 5
    
    
    def processRawHand(self, raw):
        processedHand = []
        for i in range(0, len(raw), 3):  # increments by 3 since every card is Value-Suit-Space
            processedHand.append([self.getCardValue(raw[i]), self.getCardValue(raw[i+1])])
        return processedHand
    
    
    def getCardValue(self, c):  # converts both card face/value and suit to a number
        if (ord(c) < 65):  # if c is between 2-9 return that value
            return int(c)
        conversion = {
            "T": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
            "C": 0,  # clubs
            "D": 1,  # diamonds
            "H": 2,  # hearts
            "S": 3   # spades
        }
        return conversion.get(c)
    
    
    def compare(self, hand2):
        equiv1 = self.convert()  # equivalent array of hand1
        equiv2 = hand2.convert()  # equivalent array of hand2
        traverser = 0
        while (traverser < self.SIZE):
            if (traverser == len(equiv1)):
                return 0  # Neither player wins
            if (equiv1[traverser] > equiv2[traverser]):
                return 1  # Player one wins
            elif (equiv1[traverser] == equiv2[traverser]):
                traverser += 1
            else:
                return -1  # player two wins
      
      
    def convert(self):
        self.pokerSort()
        if (self.allSuitSame()):  # we seperate flushes from non-flushes
            return self.straightArray(8, 5)  # 8 for straight-flush, 5 for plain flush
        return self.convertDiffSuit()
            

    def convertDiffSuit(self):
        repeats = self.getRepeats()
        if (len(repeats) == 0):  # either a high-card hand or a straight
            return self.straightArray(4, 0)  # 4 is a regular straight, 0 is a high card hand
            
        if (repeats[0][1] == 4):  # four of a kind
            return [7, repeats[0][0]]
        
        if (repeats[0][1] == 3):  # three of a kind or full house
            return self.threeRepArray(repeats)
            
        if (len(repeats) == 1):  # pair
            return self.pairArray(repeats)

        return self.twoPairArray(repeats)  # we have checked every case but two pair
    
    
    def twoPairArray(self, repeats):
        retval = [2, repeats[0][0], repeats[1][0]]
        for i in range(0, self.SIZE):
            if (self.hand[i][0] != repeats[0][0] and self.hand[i][0] != repeats[1][0]):
                retval.append(self.hand[i][0])
        return retval
        
        
    def pairArray(self, repeats):
        retval = [1, repeats[0][0]]
        for i in range(0, self.SIZE):
            if (self.hand[i][0] != repeats[0][0]):
                retval.append(self.hand[i][0])
        return retval
        
        
    def threeRepArray(self, repeats):
        if (len(repeats) == 1):  # 3 of a kind, returns [3, repeat card, higher card, lower card]
            retval = [3, repeats[0][0]]
            for i in range(0, self.SIZE):
                if (self.hand[i][0] != repeats[0][0]):
                    retval.append(self.hand[i][0])
            return retval
            
        return [6, repeats[0][0], repeats[1][0]]  # full house, returns [6, 3 repeat card, 2 repeat card]
        
        
    def straightArray(self, trueWeight, falseWeight):
        straightVal = self.isStraight()
        if (straightVal == 1):
            return [trueWeight, self.hand[0][0]]  # highest card of the straight
            
        elif (straightVal == 2):
            return [trueWeight, self.hand[1][0]]  # 14-5-4-3-2 (A2345) returns 5
            
        retval = [falseWeight]
        for i in range(0, self.SIZE):
            retval.append(self.hand[i][0])
        return retval
        
        
    def isStraight(self):  # 0 = no straight, 1 = normal straight, 2 = wheel straight
        for i in range(0, self.SIZE-1):
            case1 = self.hand[i][0] == self.hand[i+1][0]+1  # regular straight
            case2 = i == 0 and self.hand[i][0] == self.hand[i+1][0]+9  # 14, 5, 4, 3, 2
            if (not case1 and not case2):
                return 0
                break
        
        if (self.hand[0][0] == self.hand[1][0]+9):
            return 2
        return 1

            
    def getRepeats(self):  # Cases: 4, 3-2, 3, 2-2, 2
        repeats = []
        count = 1
        for i in range(0, self.SIZE):
            if (i != self.SIZE-1 and self.hand[i][0] == self.hand[i+1][0]):
                count += 1
            elif (count > 1):
                if (count > 2):  # Cases: 4, 3-2, 3
                    repeats.insert(0, [self.hand[i][0], count])
                elif (count == 2):  # Cases: 2-2, 2
                    repeats.append([self.hand[i][0], count])
                count = 1
                        
        return repeats
        
                                
    def pokerSort(self):  # Returns list sorted in descending order by card value
        self.hand = sorted(self.hand, key=itemgetter(0), reverse=True)


    def allSuitSame(self):  # Checks if all suits are the same in a hand
        for i in range(0, self.SIZE-1):
            if (self.hand[i][1] != self.hand[i+1][1]):
                return False
        return True
    
    
    def __str__(self):
        return str(self.hand)
    


# ------------------- Program begins here -------------------
caseCount = int(input())
for i in range(0, caseCount):
    line = input()
    h1 = Poker_Hand(line[0:15])  # Gets the first 15 chars which is the first hand
    h2 = Poker_Hand(line[15:])
    if (h1.compare(h2) == 1):
        print("Player 1")
    else:
        print("Player 2")
    
