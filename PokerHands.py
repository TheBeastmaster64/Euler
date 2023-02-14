from operator import itemgetter
class Poker_Hand:
    def __init__(self, hand): #Hand is the set of 5 cards one has
        self.hand = self.process_raw_hand(hand)
        self.SIZE = 5
    
    def process_raw_hand(self, raw):
        processed_hand = []
        for i in range(0, len(raw), 3): #increments by 3 since every card is Value-Suit-Space
            processed_hand.append([self.get_card_value(raw[i]), self.get_card_value(raw[i+1])])
        return processed_hand
    
    def get_card_value(self, c): #By alphabetical order: 0 = Clubs, 1 = Diamonds, 2 = Hearts, 3 = Spades
        if(ord(c) < 65): #If c is between 2-9 return that value
            return int(c)
        conversion = {
            "T": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14,
            "C": 0,
            "D": 1,
            "H": 2,
            "S": 3
        }      
        return conversion.get(c)
    
    def compare(self, hand2): #The format of returned arrays for hands are as follows: [number correstponding to type of hand, most important high value, second most important high value...]
        #TODO: When looking for what type of hand there is, start with best one (i.e., check for royal flush, then straight flush, etc.)
        equiv1 = self.convert() #equivalent array of hand1 
        equiv2 = hand2.convert() #equivalent array of hand2
        traverser = 0
        while(True):
            if(traverser == len(equiv1)):
                return 0 #Neither player wins since if it traversed equal arrays until it is greater than one of them, the two arrays are equal by the format here
            if(equiv1[traverser] > equiv2[traverser]):
                return 1 #Player one wins
            elif(equiv1[traverser] == equiv2[traverser]):
                traverser += 1
            else:
                return -1 #Player two wins
      
    def convert(self):
        self.poker_sort()
        hand_val = []
        if(self.all_suit_same()):
            return self.convert_same_suit()
        return self.convert_diff_suit()
            
    def convert_same_suit(self): #5 = flush, 8 = straight flush and royal flush since royal flush is the strongest straight flush
        flag = True #Royal flush case
        straight_val = self.is_straight()
        if(straight_val == 1):
            return [8, self.hand[0][0]] #highest value
        elif(straight_val == 2):
            return [8, self.hand[1][0]] #highest value
        retval = [5]
        for i in range(0, self.SIZE):
            retval.append(self.hand[i][0])
        return retval
        
    def convert_diff_suit(self): #0 = high card, 1 = pair, 2 = two pair, 3 = three of a kind, 4 = straight,  6 = full house, 7 = four of a kind,
        repeats = self.get_repeats()
        if(len(repeats) == 0):
            straight_val = self.is_straight()
            if(straight_val == 1):
                return [4, self.hand[0][0]] #highest value
            elif(straight_val == 2):
                return [4, self.hand[1][0]] #highest value
            retval = [0] #Dog hand
            for i in range(0, self.SIZE):
                retval.append(self.hand[i][0])
            return retval
        if(repeats[0][1] == 4): #Four of a kind
            return [7, repeats[0][0]]
        elif(repeats[0][1] == 3): #Three of a kind or full house
            if(len(repeats) == 1): #Three of a kind
                retval = [3, repeats[0][0]]
                for i in range(0, self.SIZE):
                    if(self.hand[i][0] != repeats[0][0]):
                        retval.append(self.hand[i][0])
                return retval
            return [6, repeats[0][0], repeats[1][0]] #full house
        if(len(repeats) == 1): #Pair
            retval = [1, repeats[0][0]] 
            for i in range(0, self.SIZE):
                if(self.hand[i][0] != repeats[0][0]):
                    retval.append(self.hand[i][0])
            return retval
        retval = [2, repeats[0][0], repeats[1][0]] #Two pair
        for i in range(0, self.SIZE):
            if(self.hand[i][0] != repeats[0][0] and self.hand[i][0] != repeats[1][0]):
                retval.append(self.hand[i][0])
        return retval
        
    def is_straight(self): #0 = no straight, 1 = normal straight, 2 = wheel straight
        flag = True  #Straight flush case
        for i in range(0, self.SIZE-1):
            if(i == 0 and self.hand[i][0] != self.hand[i+1][0]+1 and self.hand[i][0] != self.hand[i+1][0]+9): #14, 5, 4, 3, 2 is still straight flush
                flag = False
                break
            if(i > 0 and self.hand[i][0] != self.hand[i+1][0]+1):
                flag = False
                break
        if(flag): #The if statements here are because of that weird flush
            if(self.hand[i][0] == self.hand[i+1][0]+9):
                return 2
            return 1
        return 0
            
    def get_repeats(self):
        repeats = []
        for i in range(0, self.SIZE-1):
            current_count = 1
            for j in range(i+1, self.SIZE):
                if(self.hand[i][0] == self.hand[j][0]):
                    current_count += 1
            if(current_count > 1):
                if(len(repeats) == 1):
                    if(current_count > repeats[0][1]):
                        repeats.insert(0, [self.hand[i][0], current_count])
                    elif(current_count == repeats[0][1] and self.hand[i][0] > repeats[0][0]): #If they repeat the same time but the new repeat has a greater value than the previous
                        repeats.insert(0, [self.hand[i][0], current_count])
                    elif(self.hand[i][0] != repeats[0][0]):
                        repeats.append([self.hand[i][0], current_count])
                else:
                    repeats.append([self.hand[i][0], current_count])
        return repeats
                                
    def poker_sort(self):
        self.hand = sorted(self.hand, key=itemgetter(0), reverse = True)

    def all_suit_same(self): #Checks if all suits are the same in a hand
        for i in range(0, self.SIZE-1):
            if(self.hand[i][1] != self.hand[i+1][1]):
                return False
        return True
        
    def __str__(self):
        return str(self.hand)   
    
    
    
    
    
#def convert_hand_to_val(hand): #Converts the poker hand to a numerical value (e.g., royal flush = 6 or smth)
    
    
    
#def winner(hand1, hand2): 
file1 = open("../Files/p054_poker.txt", "r")
lines = file1.readlines()
count = 0
for i in range(0, len(lines)):
    h1 = Poker_Hand(lines[i][0:15]) #Gets the first 15 chars which is the first hand
    h2 = Poker_Hand(lines[i][15:])
    if(h1.compare(h2) == 1):
        count += 1
    
print(count)
file1.close()
