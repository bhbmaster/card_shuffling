from card import Card
import random

# SIDENOTE: could have made easy deck like this
# make a deck of cards using itertools
# import itertools, random
# deck = list(itertools.product(['ACE',2,3,4,5,6,7,8,9,10,"JACK","QUEEN","KING"],['Spade','Heart','Diamond','Club']))
# # deck = [('ACE', 'Spade'), ('ACE', 'Heart'), ('ACE', 'Diamond'), ('ACE', 'Club'), (2, 'Spade'), (2, 'Heart'), (2, 'Diamond'), (2, 'Club'), (3, 'Spade'), (3, 'Heart'), (3, 'Diamond'), (3, 'Club'), (4, 'Spade'), (4, 'Heart'), (4, 'Diamond'), (4, 'Club'), (5, 'Spade'), (5, 'Heart'), (5, 'Diamond'), (5, 'Club'), (6, 'Spade'), (6, 'Heart'), (6, 'Diamond'), (6, 'Club'), (7, 'Spade'), (7, 'Heart'), (7, 'Diamond'), (7, 'Club'), (8, 'Spade'), (8, 'Heart'), (8, 'Diamond'), (8, 'Club'), (9, 'Spade'), (9, 'Heart'), (9, 'Diamond'), (9, 'Club'), (10, 'Spade'), (10, 'Heart'), (10, 'Diamond'), (10, 'Club'), ('JACK', 'Spade'), ('JACK', 'Heart'), ('JACK', 'Diamond'), ('JACK', 'Club'), ('QUEEN', 'Spade'), ('QUEEN', 'Heart'), ('QUEEN', 'Diamond'), ('QUEEN', 'Club'), ('KING', 'Spade'), ('KING', 'Heart'), ('KING', 'Diamond'), ('KING', 'Club')]
# random.shuffle(deck) # can shuffle like this

class Deck:

    def __init__(self, list_of_cards):
        self.cards = list_of_cards

    @classmethod
    def create_joker_deck_numbered(cls): # 2 jokers (sort order: numbers -> suits, ex: HA, SA, CA, DA, H2, S2, C2, D2, H3, S3, C3, D3 ...)
        deck = []
        for i_v in Card._values:
            for i_s in Card._suits:
                try:
                    CARD = Card(i_v, i_s)
                except:
                    continue
                deck.append(CARD)
                if i_s == "JOKER": # if joker add it again for 2
                    deck.append(CARD)
        return cls(deck)

    @classmethod
    def create_clean_deck_numbered(cls): # clean (sort order: numbers -> suits, ex: HA, SA, CA, DA, H2, S2, C2, D2, H3, S3, C3, D3 ...)
        d = []
        for i_v in Card._values:
            for i_s in Card._suits:
                try:
                    CARD = Card(i_v, i_s)
                except:
                    continue
                d.append(CARD)
        d.pop() # pop the last joker out
        return cls(d)

    @classmethod
    def create_joker_deck_suited(cls): # 2 jokers (sort order: suite -> numbers, ex: HA,H2,H3,...DJ,DQ,DK,JKR,JKR)
        deck = []
        for i_s in Card._suits:
            for i_v in Card._values:
                try:
                    CARD = Card(i_v, i_s)
                except:
                    continue
                deck.append(CARD)
                if i_s == "JOKER": # if joker add it again for 2
                    deck.append(CARD)
        return cls(deck)

    @classmethod
    def create_clean_deck_suited(cls): # clean (sort order: suite -> numbers, ex: HA,H2,H3,...DJ,DQ,DK)
        deck = []
        for i_s in Card._suits:
            for i_v in Card._values:
                try:
                    CARD = Card(i_v, i_s)
                except:
                    continue
                deck.append(CARD)
        deck.pop() # pop the last joker out
        return cls(deck)

    def shuffle_deck_random(self): # shuffle with pythons random module (computer shuffle)
        random.shuffle(self.cards)

    @staticmethod
    def chunk_out_cards(cards, lower_bound_size_of_chunk, upper_bound_size_of_chunk):
        # lower_bound_size_of_chunk = lower # in a perfect world both these are 1
        # upper_bound_size_of_chunk = upper # as every card is chunked
        count = len(cards)
        start_index = final_index = 0
        # while start_index < count and final_index < count:
        chunks = []
        while final_index <= count-1:   # 26 < 26
            chunk_size = random.randint(1,3)
            final_index = start_index + chunk_size  # 26 + 1 --> 27
            if final_index >= count+1:   # 27 >= 28
                final_index = count
            # print("cs", chunk_size, "|",start_index, "->", final_index, list(range(start_index,final_index)), "count:", count, start_index < count, final_index < count, " ->", start_index < count or final_index < count)
            chunk = cards[start_index:final_index] # note items included are [start_index,final_index) so final_index is not included
            chunks.append(chunk)
            start_index += chunk_size
            # print("TO NEXT LOOP:", chunk_size, "|",start_index, "->", final_index, list(range(start_index,final_index)), "count:", count, start_index < count, final_index < count, " ->", start_index < count or final_index < count)
        # print(f"{cards=}")
        # print(f"{chunks=}")
        return chunks


        # false False --> stop
        # true True  --> run
        # false True --> stop
        # true false --> stop

    def shuffle_deck_bridge(self): # shuffle like human using bridge (human shuffle)
        lower_bound_size_of_chunk = 1
        upper_bound_size_of_chunk = 3
        shuffle_with_left_hand_first = random.choice([True, False]) # left is hand1, right is hand2
        count = len(self.cards)
        half_index = len(self.cards) // 2
        # note: top card is index 0
        ### print(f"{half_index=} {type(half_index)}")
        half1 = self.cards[:half_index]
        half2 = self.cards[half_index:]
        ### print(f"{half1=} {len(half1)=}")
        ### print(f"{half2=} {len(half2)=}")
        # google split list in chunks and look at this for next steps.
        # >>> import deck
        # >>> D1 = deck.Deck.create_joker_deck_numbered()
        # >>> D1.shuffle_deck_bridge()
        # half_index=26 <class 'int'>
        # half1=[A♡, A♠, A♣, A♢, 2♡, 2♠, 2♣, 2♢, 3♡, 3♠, 3♣, 3♢, 4♡, 4♠, 4♣, 4♢, 5♡, 5♠, 5♣, 5♢, 6♡, 6♠, 6♣, 6♢, 7♡, 7♠] len(half1)=26
        # half2=[7♣, 7♢, 8♡, 8♠, 8♣, 8♢, 9♡, 9♠, 9♣, 9♢, 10♡, 10♠, 10♣, 10♢, J♡, J♠, J♣, J♢, Q♡, Q♠, Q♣, Q♢, K♡, K♠, K♣, K♢, JKR] len(half2)=27
        # print("---half1 chunking---")
        half1_chunked = self.chunk_out_cards(half1,lower_bound_size_of_chunk,upper_bound_size_of_chunk)
        # print("---half2 chunking---")
        half2_chunked = self.chunk_out_cards(half2,lower_bound_size_of_chunk,upper_bound_size_of_chunk)
        # print("--------------------")
        ### print(f"{half1_chunked=}\n{half2_chunked=}")
        # now we combine both chunks start with half1 or half2 and alternate the index
        # half1=[A♡, 2♡, 3♡, 4♡, 5♡, 6♡, 7♡, 8♡, 9♡, 10♡, J♡, Q♡, K♡, A♠, 2♠, 3♠, 4♠, 5♠, 6♠, 7♠, 8♠, 9♠, 10♠, J♠, Q♠, K♠, A♣] len(half1)=27
        # half2=[2♣, 3♣, 4♣, 5♣, 6♣, 7♣, 8♣, 9♣, 10♣, J♣, Q♣, K♣, A♢, 2♢, 3♢, 4♢, 5♢, 6♢, 7♢, 8♢, 9♢, 10♢, J♢, Q♢, K♢, JKR, JKR] len(half2)=27
        # half1_chunked=[[A♡, 2♡, 3♡], [4♡], [5♡, 6♡, 7♡], [8♡, 9♡, 10♡], [J♡], [Q♡], [K♡, A♠, 2♠], [3♠, 4♠, 5♠], [6♠, 7♠], [8♠], [9♠], [10♠], [J♠], [Q♠, K♠], [A♣]]
        # half2_chunked=[[2♣, 3♣], [4♣, 5♣], [6♣, 7♣, 8♣], [9♣], [10♣, J♣, Q♣], [K♣, A♢, 2♢], [3♢], [4♢, 5♢, 6♢], [7♢, 8♢, 9♢], [10♢, J♢], [Q♢, K♢], [JKR, JKR]]
        len_h1c = len(half1_chunked)
        len_h2c = len(half2_chunked)
        i = -1
        shuffled = []
        while True:
            i += 1
            done = True
            if shuffle_with_left_hand_first:
                if i < len_h1c: # add index if can
                    shuffled.extend(half1_chunked[i])
                    done = False
                if i < len_h2c: # add index if can
                    shuffled.extend(half2_chunked[i])
                    done = False
            else:
                if i < len_h2c: # add index if can
                    shuffled.extend(half2_chunked[i])
                    done = False
                if i < len_h1c: # add index if can
                    shuffled.extend(half1_chunked[i])
                    done = False
            if done:
                break
        ### print(f"{shuffled=} {len(shuffled)=}")
        self.cards = shuffled

    def shuffle_deck_handed(self): # shuffle like one handed throw into another hand (human shuffle)
        lower_bound_size_of_chunk = 1
        upper_bound_size_of_chunk = 6
        chunked_cards = self.chunk_out_cards(self.cards,lower_bound_size_of_chunk,upper_bound_size_of_chunk)
        chunked_cards.reverse() # reversing the chunks is the essense of this type of shuffle
        flattened_list = [item for sublist in chunked_cards for item in sublist]
        self.cards = flattened_list

    def findall_number(self, number_to_find): # return indexes of specific card numbers. ex: [ "ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", None ]
        found_locations = []
        for i,v in enumerate(self.cards):
            if v.value == number_to_find:
                found_locations.append(i)
        return found_locations

    def findall_suit(self, suit_to_find): # return indexes of specific card suits. ex: [ "HEART", "SPADE", "CLUB", "DIAMOND", "JOKER" ]
        found_locations = []
        for i,v in enumerate(self.cards):
            if v.suit == suit_to_find:
                found_locations.append(i)
        return found_locations

    def analysis_distance_from_same_number(self):
        averages = []
        for v in Card._values: # iterate thru all numbers ace thru king and joker(None) if its there
            all_loc = self.findall_number(v) # get list of all locations
            if len(all_loc) == 0:
                continue
            diff_list = [] # get absolute value difference list [10,20,25] becomes [10,5]
            for i,loc in enumerate(all_loc[:-1]):
                diff = abs(all_loc[i] - all_loc[i+1])
                diff_list.append(diff)
            avg = sum(diff_list) / len(diff_list) # now get a standard mean of the differences
            averages.append(avg) # note down that mean/average for that card value
            # print(f"-- looking at all '{v}' locs:{all_loc} ds:{diff_list} avg_ds:{avg}")
        final_average = sum(averages) / len(averages) # mean all of the difference mean
        return final_average

    def __len__(self): # print how many cards
        return len(self.cards)

    def __repr__(self): # print deck of cards
        return "[ " +  ", ".join([str(i) for i in self.cards]) + " ]"

def test():
    List_Of_Decks = [ "D_clean", "D_joker", "D_clean_s", "D_joker_s"]
    D_clean = Deck.create_clean_deck_numbered()
    D_joker = Deck.create_joker_deck_numbered()
    D_clean_s = Deck.create_clean_deck_suited()
    D_joker_s = Deck.create_joker_deck_suited()
    for i in List_Of_Decks:
        current_deck = eval(i)
        print(f"* {i} d_from_cards={current_deck.analysis_distance_from_same_number()} len={len(current_deck)} {current_deck=}")
        current_deck.shuffle_deck_bridge()
        print(f"-- (1 shuffle) {i} d_from_cards={current_deck.analysis_distance_from_same_number()} len={len(current_deck)} {current_deck=}")
        current_deck.shuffle_deck_bridge()
        current_deck.shuffle_deck_bridge()
        current_deck.shuffle_deck_bridge()
        current_deck.shuffle_deck_bridge()
        print(f"-- (5 shuffle) {i} **d_from_cards={current_deck.analysis_distance_from_same_number()}** len={len(current_deck)} {current_deck=}")
        print()

if __name__ == "__main__":
    test() # comment out if dont want tests
    pass

# EOF