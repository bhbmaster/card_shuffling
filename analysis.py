from deck import Deck

def main():
    max_shuffles = 10
    List_Of_Decks = [ "D_clean", "D_joker", "D_clean_s", "D_joker_s"]
    D_clean = Deck.create_clean_deck_numbered()
    D_joker = Deck.create_joker_deck_numbered()
    D_clean_s = Deck.create_clean_deck_suited()
    D_joker_s = Deck.create_joker_deck_suited()
    for i in List_Of_Decks:
        current_deck = eval(i)
        print(f"-- {i} --")
        print(f"pre deck:  {current_deck}")
        d_avg=current_deck.analysis_distance_from_same_number()
        print(f"* [shuff_num, d_avg] = [0, {d_avg:0.4f}]", end="")
        for i in range(1,max_shuffles):
            current_deck.shuffle_deck_bridge()
            d_avg=current_deck.analysis_distance_from_same_number()
            print(f" [{i}, {d_avg:0.4f}]", end="")
        print()
        print(f"post deck: {current_deck}")
        print()
        print()

if __name__ == "__main__":
    main() # comment out if dont want tests
    pass

# EOF