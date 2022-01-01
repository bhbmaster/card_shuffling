from deck import Deck

def main():
    max_shuffles = 100
    List_Of_Decks = [ "D_clean", "D_joker", "D_clean_s", "D_joker_s"]
    D_clean = Deck.create_clean_deck_numbered()
    D_joker = Deck.create_joker_deck_numbered()
    D_clean_s = Deck.create_clean_deck_suited()
    D_joker_s = Deck.create_joker_deck_suited()
    percision = 3
    for i in List_Of_Decks:
        current_deck = eval(i)
        print(f"-- {i} --")
        print(f"* initial deck: {current_deck}")
        current_deck.nice_output(print_to_screen=True)
        d_avg_list = []
        d_avg=current_deck.analysis_distance_from_same_number()
        d_avg_list.append(d_avg)
        print(f"* [shuff_num, d_avg] = [0, {d_avg:0.{percision}f}]", end="")
        for i in range(1,max_shuffles):
            # current_deck.shuffle_deck_random()
            # current_deck.shuffle_deck_bridge()
            current_deck.shuffle_deck_handed()
            d_avg=current_deck.analysis_distance_from_same_number()
            d_avg_list.append(d_avg)
            print(f" [{i}, {d_avg:0.{percision}f}]", end="")
        print()
        print(f"* shuffld deck: {current_deck}")
        current_deck.nice_output(print_to_screen=True)
        print(f"* {max_shuffles} shuffles, first d_avg -> last d_avg = {d_avg_list[0]:0.{percision}f} -> {d_avg_list[-1]:0.{percision}f}")
        print()
        print()

if __name__ == "__main__":
    main() # comment out if dont want tests
    pass

# EOF