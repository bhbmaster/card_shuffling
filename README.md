
# Card Shuffling Analysis

Just creating card class and deck class.
Decks can be made with and without jokers.
Trying to run different mathematical analisys on different shuffling algos. So far I have these:

- random shuffle using python library (every card randomized)
- shuffle by splitting cards around the midway point and doing a bridge, where cards intercross and combine into final shuffled deck
- shuffle by taking cards and throwing some-cards (chunks) into left hand over and over

Supported to run in *python 3.9* and newer:

```
python card.py       # creates decks of cards and tests things
python deck.py       # creates decks of cards and shuffles them
python analysis.py   # shuffles all decks of cards multiple times and provides analysis
```